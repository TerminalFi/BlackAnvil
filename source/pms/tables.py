import django_tables2 as tables
from .models import Projects, TesterWork, ProjectTester


class ProjectsTable(tables.Table):

    class Meta:
        model = Projects
        template_name = 'tables/table.html'
        row_attrs = {
            'data-id': lambda record: record.pk
        }
        sequence = ('id', 'client_name', 'project_name',
                    'project_total_hours', 'project_charge_code')
        exclude = ['project_notes', 'client_department',
                   'client_phone', 'project_comments']


class ProjectTesterTable(tables.Table):
    user_id = tables.Column(verbose_name='User ID')

    class Meta:
        model = ProjectTester
        template_name = 'tables/project_tester_table.html'
        row_attrs = {
            'data-id': lambda record: record.pk
        }
        sequence = ('id', 'user_id',
                    'assigned_hours')
        exclude = ['project_id']


class TesterWorkTable(tables.Table):
    user_id = tables.Column(verbose_name='User ID')

    class Meta:
        model = TesterWork
        template_name = 'tables/tester_work_table.html'
        sequence = ('id', 'user_id', 'task',
                    'consumed_hours')
        exclude = ['project_id']