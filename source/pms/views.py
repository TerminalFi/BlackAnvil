from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, TemplateView
from django.views.generic.edit import (CreateView, UpdateView,
                                       DeleteView)
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.http import JsonResponse
from django.db.models import Count, Sum

from datetime import datetime

from django_tables2.views import SingleTableMixin
import django_tables2 as tables

from .forms import ProjectForm
from .tables import ProjectsTable
from .models import Projects



class ProjectIndexView(LoginRequiredMixin, tables.SingleTableView):
    template_name = 'index.html'
    table_class = ProjectsTable
    queryset = Projects.objects.all()
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(ProjectIndexView, self).get_context_data(**kwargs)
        project_data = Projects.objects.aggregate(
            Count('id'), Sum('project_total_hours'))
        context['total_projects'] = project_data['id__count']
        context['total_hours'] = project_data['project_total_hours__sum']
        return context



class NewProjectView(LoginRequiredMixin, CreateView):
    template_name = 'new_project.html'
    form_class = ProjectForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.project_remaining_hours = self.request.POST['project_total_hours']
        obj.save()
        messages.success(self.request, _(
            'Project successfully created!'))
        return super().form_valid(form)


class UpdateProjectView(LoginRequiredMixin, UpdateView):
    template_name = 'update_project.html'
    form_class = ProjectForm
    model = Projects
    success_url = reverse_lazy('pms:view_projects')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.project_remaining_hours = self.request.POST['project_total_hours']
        obj.project_notes = obj.project_notes
        obj.save()
        messages.success(self.request, _(
            'Project successfully updated!'))
        self.success_url = self.request.POST['next']
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(UpdateProjectView, self).get_context_data(**kwargs)
        context['project_id'] = self.kwargs.get('pk')
        return context


class DeleteProjectView(DeleteView):
    success_url = reverse_lazy('index')
    model = Projects

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, _(
            'Project deleted successfully!'))
        return super(DeleteProjectView, self).delete(request, *args, **kwargs)


class NoteUpdate(View):
    success_url = reverse_lazy('index')

    def post(self, request, pk):
        now = datetime.now().strftime('%D - %H:%M:%S')
        user = "{0} {{{1}}}".format(self.request.user.get_full_name(), self.request.user.username)
        data = dict()
        note = Projects.objects.get(pk=pk)
        if note and len(self.request.POST['new_note'].lstrip()) > 0:
            new_note = "{0}{1} | {2} | {3}\n".format(
                note.project_notes, now, user, self.request.POST['new_note'])
            note.project_notes = new_note
            note.save()
            data['message'] = new_note
        else:
            data = JsonResponse({"Error": "There was an error"})
            data.status_code = 403
            return data
        return JsonResponse(data)
