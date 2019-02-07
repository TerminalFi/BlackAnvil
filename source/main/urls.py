from django.urls import path, include

from .views import IndexPageView, contact_us

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('contact/', contact_us, name='contact'),
]