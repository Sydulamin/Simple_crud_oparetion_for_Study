from django.urls import path
from .views import hello, all_prof, delete_prof, Update

urlpatterns = [
    path('', hello, name='hello'),
    path('all_prof/', all_prof, name='all_prof'),
    path('delete_prof/<int:id>/', delete_prof, name='delete_prof'),
    path('Update/<int:id>/', Update, name='Update'),
]
