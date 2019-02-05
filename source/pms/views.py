from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group
from django.views.generic.edit import (CreateView, UpdateView,
                                       DeleteView)
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.db.models import Count, Sum
from django.db.models.functions import Coalesce
import django_tables2 as tables

from .forms import ProjectForm
from .tables import ProjectsTable
from .models import Projects


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
class ProjectManageView(LoginRequiredMixin, tables.SingleTableView):
    template_name = 'manage_project.html'
    table_class = ProjectsTable
    queryset = Projects.objects.all()
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(ProjectManageView, self).get_context_data(**kwargs)
        project_data = Projects.objects.filter(pk=self.kwargs.get('pk')).aggregate(
            total_hours=Coalesce(Sum('project_total_hours'), 0))
        context['total_hours'] = project_data['total_hours']
        return context

    def get_queryset(self):
        return Projects.objects.filter(pk=self.kwargs.get('pk'))


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
