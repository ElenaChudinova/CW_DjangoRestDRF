from django.shortcuts import get_object_or_404
from django_celery_beat.utils import now_localtime
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from users.permissions import IsModer, IsOwner

from .models import Habit
from .paginators import CustomPagination
from .serializers import HabitSerializer
from habit.tasks import send_inform_habit


class UserHabitViewSet(ModelViewSet):
    queryset = Habit.objects.filter(in_publicity=True)
    serializer_class = HabitSerializer
    pagination_class = CustomPagination

    @action(methods=['get'], detail=True)  # Указываешь методы и что это действие для одного объекта
    def time_lead(self, request, pk=None):  # pk должен быть опциональным (detail=True)
        habit = get_object_or_404(Habit, pk=pk)
        if habit.time_lead.filter(pk=request.user.pk) == now_localtime:
            send_inform_habit.delay(habit.user.email)
        serializer = self.get_serializer(habit)
        return Response(data=serializer.data)


class HabitCreateAPIView(CreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (
        IsAuthenticated,
        ~IsModer,
    )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HabitListAPIView(ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (
        IsAuthenticated,
        IsModer | IsOwner,
    )
    pagination_class = CustomPagination

    def get(self, request):
        habits = Habit.objects.filter(user=request.user)
        serializer = HabitSerializer(habits, many=True)
        return Response(serializer.data)


class HabitRetrieveAPIView(RetrieveAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (
        IsAuthenticated,
        IsModer | IsOwner,
    )


class HabitUpdateAPIView(UpdateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (
        IsAuthenticated,
        IsModer | IsOwner,
    )


class HabitDestroyAPIView(DestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (
        IsAuthenticated,
        IsOwner | ~IsModer,
    )
