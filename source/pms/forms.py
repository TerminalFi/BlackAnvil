from django import forms
from django.forms import ModelForm
from .models import Projects, ProjectTester, UserFullName, TesterWork


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
    user_id = forms.ModelChoiceField(
        queryset=UserFullName.objects.all(), label="Username")

    class Meta:
        model = ProjectTester
        fields = ['user_id', 'assigned_hours']
        exclude = ['project_id']
        labels = {'user_id': 'User ID',
                  'assigned_hours': 'Assigned Hours'}


class AssignmentChargeForm(ModelForm):
    charge_code = forms.CharField(label="Charge Code", required=True)

    class Meta:
        model = TesterWork
        fields = ['task', 'consumed_hours']
        exclude = ['project_id', 'user_id']
        labels = {'user_id': 'User ID',
                  'consumed_hours': 'Hours'}
