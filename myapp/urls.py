from myapp.views import greeting
from myapp.views import hello_user

from django.urls import path
from .views import SubTaskListCreateView, SubTaskDetailUpdateDeleteView


urlpatterns = [
    path('', greeting, name='greeting'),
    path('', hello_user, name='hello'),

    path('subtasks/', SubTaskListCreateView.as_view(), name='subtask-list-create'),
    path('subtasks/<int:pk>/', SubTaskDetailUpdateDeleteView.as_view(), name='subtask-detail-update-delete'),
]



