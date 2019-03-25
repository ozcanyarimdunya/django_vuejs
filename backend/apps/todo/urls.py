from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [
    path('list/', views.TodoList.as_view(), name='list'),
    path('create/', views.TodoCreate.as_view(), name='create'),
    path('detail/<int:pk>/', views.TodoDetail.as_view(), name='detail'),
    path('update/<int:pk>/', views.TodoUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', views.TodoDelete.as_view(), name='delete'),
    path('toggle/<int:pk>/', views.TodoToggle.as_view(), name='toggle'),
]

from rest_framework import routers
from django.urls import include

router = routers.DefaultRouter()
router.register(r'vs', views.TodoViewSet)
urlpatterns += [
    path('', include(router.urls))
]
