from rest_framework.routers import DefaultRouter
from myapp.views import greeting, TaskListCreateView, TaskRetrieveUpdateDestroyView, SubTaskRetrieveUpdateDestroyView, \
    CategoryViewSet, TaskStatsView, UserTaskListView, UserSubTaskListView
from myapp.views import hello_user
from django.urls import path, include
from .views import SubTaskListCreateView
from rest_framework.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Your Project API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@yourproject.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

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
    path('', include(router.urls)),
    path('user/tasks/', UserTaskListView.as_view(), name='user-tasks'),
    path('user/subtasks/', UserSubTaskListView.as_view(), name='user-subtasks'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]



