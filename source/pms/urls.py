from django.urls import path
from .views import (ProjectIndexView, ProjectManageView,
                    NewProjectView, DeleteProjectView, UpdateProjectView)

app_name = 'pms'

urlpatterns = [
    path('', ProjectIndexView.as_view(), name='index'),
    path('projects/manage/<int:pk>/',
         ProjectManageView.as_view(), name='manage_project'),
    path('projects/new/',
         NewProjectView.as_view(), name='new_project'),
    path('projects/update/<int:pk>/',
         UpdateProjectView.as_view(), name='update_project'),
    path('projects/delete/<int:pk>/',
         DeleteProjectView.as_view(), name='delete_project'),
]
