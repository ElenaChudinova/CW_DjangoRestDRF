from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habit.models import Habit
from users.models import User

class HabitTestCase(APITestCase):
    """Тест CRUD для класса Урок."""

    def setUp(self):
        self.user = User.objects.create(email="admin@sky.pro")
        self.habit = Habit.objects.create(
            action="Зарядка для глаз", user=self.user
        )
        self.client.force_authenticate(user=self.user)

    def test_habit_retrieve(self):
        url = reverse("habit:habit_retrieve", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(data.get("action"), self.habit.action)

    def test_habit_create(self):
        url = reverse("habit:habit_create")
        data = {
            "action": "Python - знакомство с языком",
            "time_lead": "14:30:00.500",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 1)

    def test_habit_update(self):
        url = reverse("habit:habit_update", args=(self.habit.pk,))
        data = {"action": "Разминка шеи"}
        response = self.client.patch(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("action"), "Алгоритмы разминки шеи")

    def test_habit_delete(self):
        url = reverse("habit:habit_delete", args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)
