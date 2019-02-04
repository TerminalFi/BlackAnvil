from django.urls import path
from .views import (NewProjectView, DeleteProjectView,
                    UpdateProjectView, NoteUpdate)

from .views import ProjectIndexView


app_name = 'pms'

urlpatterns = [
    path('', ProjectIndexView.as_view(), name='index'),
    path('update/note/<int:pk>/', NoteUpdate.as_view(), name='update_note'),
    path('new-project/', NewProjectView.as_view(), name='new_project'),
    path('update-projects/<int:pk>/',
         UpdateProjectView.as_view(), name='update_project'),
    path('view-projects/', ProjectIndexView.as_view(), name='view_projects'),
    path('delete-project/<int:pk>/',
         DeleteProjectView.as_view(), name='delete_project'),
]
