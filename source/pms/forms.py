from django import forms
from django.forms import ModelForm
from .models import Projects, ProjectTester


class ProjectForm(ModelForm):
    client_name = forms.CharField(
        required=False)
    client_department = forms.CharField(
        required=False)
    client_phone = forms.CharField(
        required=False)
    project_comments = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Comments'}),
        required=False)

    class Meta:
        model = Projects
        fields = ['project_name', 'client_name', 'client_department',
                  'client_phone', 'project_total_hours', 'project_comments']
        exclude = ['project_notes']


class ProjectTesterForm(ModelForm):

    class Meta:
        model = ProjectTester
        fields = ['user_id', 'assigned_hours']
        exclude = ['project_id']
        labels = {'user_id': 'User ID',
                  'assigned_hours': 'Assigned Hours'}
