from django.urls import path
from .views import (ProjectIndexView, ProjectManageView,
                    NewProjectView, DeleteProjectView, ProjectAssignView,
                    UpdateProjectView, DeleteProjectAssignView,
                    AssignmentIndexView, AssignmentChargeView,
                    validate_charge_code)

app_name = 'pms'

urlpatterns = [
    path('', ProjectIndexView.as_view(), name='index'),
    path('projects/manage/<int:pk>/',
         ProjectManageView.as_view(), name='manage_project'),
    path('projects/manage/<int:pk>/assign/',
         ProjectAssignView.as_view(), name='assign_project'),
    path('projects/manage/<int:pk>/delete/tester/',
         DeleteProjectAssignView.as_view(), name='unassign_project'),
    path('projects/new/',
         NewProjectView.as_view(), name='new_project'),
    path('projects/update/<int:pk>/',
         UpdateProjectView.as_view(), name='update_project'),
    path('projects/delete/<int:pk>/',
         DeleteProjectView.as_view(), name='delete_project'),






    path('projects/assignments/',
         AssignmentIndexView.as_view(), name='assignment_index'),
    path('projects/assignments/<int:pk>/charge/',
         AssignmentChargeView.as_view(), name='assignment_charge'),



    path('projects/validate/charge/code/',
         validate_charge_code, name='validate_charge'),


]
