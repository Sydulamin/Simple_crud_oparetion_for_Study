from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from Scheduler import views as sch_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('nafi.urls')),

    path('scheduler/', sch_views.add_task, name='add_task'),
    path('task_list/', sch_views.ToDo, name='task_list'),
    path('edit_task/<int:task_id>/', sch_views.edit_task, name='edit_task'),
    path('update-task-status/<int:task_id>/', sch_views.update_task_status, name='update_task_status'),
    path('delete_task/<int:task_id>/', sch_views.delete_task, name='delete_task'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
