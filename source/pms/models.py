from django.db import models
from django.contrib.auth.models import User


class Projects(models.Model):
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
    project_notes = models.TextField(
        max_length=25000, blank=True, verbose_name='Notes')

    def __str__(self):
        return "%s" % (self.project_name)

    class Meta:
        ordering = ['id']
