from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

admin.site.site_header = settings.SITE_HEADER
admin.site.site_title = settings.SITE_HEADER

# base applications
urlpatterns = [
    path('admin/', admin.site.urls),
    path('obtain-token/', obtain_jwt_token),
    path('refresh-token/', refresh_jwt_token),
]

# my applications
urlpatterns += [
    path('todo/', include('apps.todo.urls')),
]

# all rest urls
urlpatterns += [
    path('', TemplateView.as_view(template_name='index.html'))
]

if settings.DEBUG:
    pass
