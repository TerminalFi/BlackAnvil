from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group
from django.views.generic.base import TemplateView
from django.views.generic.edit import (CreateView, UpdateView,
                                       DeleteView)
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.http import JsonResponse
from django.db.models import Count, Sum
from django.db.models.functions import Coalesce
import django_tables2 as tables
from django_tables2 import MultiTableMixin

from .forms import ProjectForm, ProjectTesterForm
from .tables import ProjectsTable, TesterWorkTable, ProjectTesterTable
from .models import Projects, TesterWork, ProjectTester


@method_decorator(
    user_passes_test(lambda u: u.is_superuser or
                     Group.objects.get(name='Project Manager') in
                     u.groups.all()), name='dispatch')
class ProjectIndexView(LoginRequiredMixin, tables.SingleTableView):
    template_name = 'index.html'
    table_class = ProjectsTable
    queryset = Projects.objects.all()
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(ProjectIndexView, self).get_context_data(**kwargs)
        project_data = Projects.objects.aggregate(
            Count('id'), total_hours=Coalesce(Sum('project_total_hours'), 0))
        context['total_projects'] = project_data['id__count']
        context['total_hours'] = project_data['total_hours']
        return context


@method_decorator(
    user_passes_test(lambda u: u.is_superuser or
                     Group.objects.get(name='Project Manager') in
                     u.groups.all()), name='dispatch')
class ProjectManageView(LoginRequiredMixin, MultiTableMixin, TemplateView):
    template_name = 'manage_project.html'
    tables = [
        ProjectsTable,
        TesterWorkTable
    ]
    table_pagination = {
        'per_page': 5
    }

    def get_tables(self):
        project = Projects.objects.filter(pk=self.kwargs.get('pk'))
        project_tester = ProjectTester.objects.filter(
            project_id=self.kwargs.get('pk'))
        tester_work = TesterWork.objects.filter(
            project_id=project.values_list('project_charge_code', flat=True)[0])
        return [
            ProjectTesterTable(project_tester),
            TesterWorkTable(tester_work),
        ]

    def get_context_data(self, **kwargs):
        project = Projects.objects.filter(pk=self.kwargs.get('pk'))
        project_charge_code = project.values_list(
            'project_charge_code', flat=True)[0]
        project_tester = ProjectTester.objects.filter(
            project_id=self.kwargs.get('pk'))

        if project_tester:
            project_tester = project_tester.aggregate(
                total_hours=Coalesce(Sum('assigned_hours'), 0))['total_hours']
            tester_worker = TesterWork.objects.filter(
                project_id=project_charge_code)
            tester_data = tester_worker.aggregate(
                total_hours=Coalesce(Sum('consumed_hours'), 0))['total_hours']
        else:
            project_tester = 0
            tester_data = 0

        context = super(ProjectManageView, self).get_context_data(**kwargs)
        project_data = project.aggregate(
            total_hours=Coalesce(Sum('project_total_hours'), 0))['total_hours']

        context['project_id'] = self.kwargs.get('pk')
        context['total_hours'] = project_data
        context['assigned_hours'] = project_tester
        context['remaining_hours'] = project_data - tester_data
        context['consumed_hours'] = tester_data
        return context


# @method_decorator(
#     user_passes_test(lambda u: u.is_superuser or
#                      Group.objects.get(name='Project Manager') in
#                      u.groups.all()), name='dispatch')
# class ProjectManageView(LoginRequiredMixin, tables.SingleTableView):
#     template_name = 'manage_project.html'
#     table_class = TesterWorkTable
#     queryset = TesterWork.objects.all()
#     paginate_by = 10

#     def get_context_data(self, **kwargs):
#         project = Projects.objects.filter(pk=self.kwargs.get('pk'))
#         project_tester = ProjectTester.objects.filter(project_id=self.kwargs.get('pk'))
#         tester_worker = TesterWork.objects.filter(
#             project_id=project.values_list('project_charge_code', flat=True)[0])
#         context = super(ProjectManageView, self).get_context_data(**kwargs)
#         project_data = project.aggregate(
#             total_hours=Coalesce(Sum('project_total_hours'), 0))['total_hours']
#         tester_data = tester_worker.aggregate(
#             total_hours=Coalesce(Sum('consumed_hours'), 0))['total_hours']

#         context['project_id'] = self.kwargs.get('pk')
#         context['total_hours'] = project_data
#         context['assigned_hours'] = project_tester.aggregate(
#             total_hours=Coalesce(Sum('assigned_hours'), 0))['total_hours']
#         context['remaining_hours'] = project_data - tester_data
#         context['consumed_hours'] = tester_data
#         return context

#     def get_queryset(self):
#         project = Projects.objects.filter(pk=self.kwargs.get('pk'))
#         project_charge_code = project.values_list('project_charge_code', flat=True)[0]
#         return TesterWork.objects.filter(project_id=project_charge_code)


@method_decorator(
    user_passes_test(lambda u: u.is_superuser or
                     Group.objects.get(name='Project Manager') in
                     u.groups.all()), name='dispatch')
class ProjectAssignView(LoginRequiredMixin, CreateView):
    template_name = 'assign_tester.html'
    form_class = ProjectTesterForm
    success_url = reverse_lazy('pms:index')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.project_id = Projects.objects.get(pk=self.kwargs.get('pk'))
        obj.save()
        self.success_url = self.request.POST['next']
        messages.success(self.request, _(
            'Project successfully created!'))
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ProjectAssignView,
                        self).get_context_data(**kwargs)
        context['project_id'] = self.kwargs.get('pk')
        return context


@method_decorator(
    user_passes_test(lambda u: u.is_superuser or
                     Group.objects.get(name='Project Manager') in
                     u.groups.all()), name='dispatch')
class DeleteProjectAssignView(DeleteView):
    success_url = reverse_lazy('pms:index')
    model = ProjectTester

    def delete(self, request, *args, **kwargs):
        self.success_url = reverse_lazy("pms:index")
        messages.success(self.request, _(
            'Tester delete from project!'))
        return super(DeleteProjectAssignView, self).delete(request, *args, **kwargs)


def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)


@method_decorator(
    user_passes_test(lambda u: u.is_superuser or
                     Group.objects.get(name='Project Manager') in
                     u.groups.all()), name='dispatch')
class NewProjectView(LoginRequiredMixin, CreateView):
    template_name = 'new_project.html'
    form_class = ProjectForm
    success_url = reverse_lazy('pms:index')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.project_remaining_hours = self.request.POST['project_total_hours']
        obj.save()
        messages.success(self.request, _(
            'Project successfully created!'))
        return super().form_valid(form)


@method_decorator(
    user_passes_test(lambda u: u.is_superuser or
                     Group.objects.get(name='Project Manager') in
                     u.groups.all()), name='dispatch')
class UpdateProjectView(LoginRequiredMixin, UpdateView):
    template_name = 'update_project.html'
    form_class = ProjectForm
    model = Projects
    success_url = reverse_lazy('pms:index')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.project_remaining_hours = self.request.POST['project_total_hours']
        obj.save()
        messages.success(self.request, _(
            'Project successfully updated!'))
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(UpdateProjectView, self).get_context_data(**kwargs)
        context['project_id'] = self.kwargs.get('pk')
        return context


@method_decorator(
    user_passes_test(lambda u: u.is_superuser or
                     Group.objects.get(name='Project Manager') in
                     u.groups.all()), name='dispatch')
class DeleteProjectView(DeleteView):
    success_url = reverse_lazy('pms:index')
    model = Projects

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, _(
            'Project deleted successfully!'))
        return super(DeleteProjectView, self).delete(request, *args, **kwargs)
