from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User


class UserFullName(User):
    class Meta:
        proxy = True

    def __str__(self):
        return "{} ({})".format(self.get_full_name(), self.username)

class Projects(models.Model):
    project_charge_code = models.UUIDField(
        unique=True,
        editable=False,
        default=uuid4,
        verbose_name="Charge Code")
    project_name = models.CharField(
        max_length=100, unique=True, default=None, verbose_name='Project Name')
    client_name = models.CharField(
        max_length=100, unique=False, default=None, verbose_name='Client Name')
    client_department = models.CharField(
        max_length=100, unique=False, default=None, verbose_name='Client Department')
    client_phone = models.CharField(
        max_length=100, unique=False, default=None, verbose_name='Client Phone')
    project_total_hours = models.IntegerField(
        default=10, verbose_name='Total Hours')
    project_comments = models.TextField(
        max_length=25000, blank=True, verbose_name='Comments')

    def __str__(self):
        return "%s" % (self.project_name)

    class Meta:
        ordering = ['-id']


class ProjectTester(models.Model):
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    assigned_hours = models.IntegerField(
        default=0, verbose_name='Assigned Hours')

    class Meta:
        ordering = ['-id']


class TesterWork(models.Model):
    project_id = models.ForeignKey(
        Projects, to_field='project_charge_code', on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.TextField(
        max_length=255, verbose_name='Task')
    consumed_hours = models.IntegerField(
        default=0, verbose_name='Hours')

    class Meta:
        ordering = ['-id']
