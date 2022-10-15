from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.TaskView.as_view(), name='taskdetail'),
    path('<int:pk>/edit', views.TaskUpdateView.as_view(), name='taskedit'),
    path('<int:pk>/delete', views.TaskDeleteView.as_view(), name='delete'),
]
