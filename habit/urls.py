from django.urls import path
from rest_framework.routers import SimpleRouter

from habit.apps import HabitConfig
from habit.views import (
    HabitCreateAPIView,
    HabitDestroyAPIView,
    HabitListAPIView,
    HabitRetrieveAPIView,
    HabitUpdateAPIView,
    UserHabitViewSet,
)

app_name = HabitConfig.name

router = SimpleRouter()
router.register("", UserHabitViewSet)

urlpatterns = [
    path("habit/", HabitListAPIView.as_view(), name="habit_list"),
    path("habit/<int:pk>/", HabitRetrieveAPIView.as_view(), name="habit_retrieve"),
    path("habit/create/", HabitCreateAPIView.as_view(), name="habit_create"),
    path("habit/<int:pk>/delete", HabitDestroyAPIView.as_view(), name="habit_delete"),
    path("habit/<int:pk>/update/", HabitUpdateAPIView.as_view(), name="habit_update"),
]

urlpatterns += router.urls
