from rest_framework.routers import DefaultRouter
from myapp.views import greeting, TaskListCreateView, TaskRetrieveUpdateDestroyView, SubTaskRetrieveUpdateDestroyView, \
    CategoryViewSet, TaskStatsView
from myapp.views import hello_user
from django.urls import path, include
from .views import SubTaskListCreateView
from rest_framework.views import TokenObtainPairView, TokenRefreshView


router = DefaultRouter()
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', greeting, name='greeting'),
    path('', hello_user, name='hello'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(), name='task-detail'),
    path('tasks/stats/', TaskStatsView.as_view(), name='task-stats'),
    path('subtasks/', SubTaskListCreateView.as_view(), name='subtask-list-create'),
    path('subtasks/<int:pk>/', SubTaskRetrieveUpdateDestroyView.as_view(), name='subtask-detail'),
    path('', include(router.urls))
]



