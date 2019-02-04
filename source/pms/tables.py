import django_tables2 as tables
from django_tables2.utils import A
from .models import Projects


class ProjectsTable(tables.Table):

    class Meta:
        model = Projects
        template_name = 'table.html'
        sequence = ('id', 'project_name', 'project_total_hours', 'client_name')
        exclude = ['project_notes', 'client_department', 'client_phone', 'project_comments']
