from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from django_celery_beat.utils import now_localtime

from config.settings import EMAIL_HOST_USER
from habit.models import Habit
from users.models import User
from habit.services import send_telegram_message


@shared_task
def send_inform_habit(email):
    """Отправляется сообщение создателю привычки о том, что необходимо выполнить привычку."""
    message = "Необходимо выполнить привычку"
    user = User.objects.get(email=email)
    if user.tg_chat_id:
        send_telegram_message(user.tg_chat_id, message)


@shared_task()
def is_active_habit():
    habits = Habit.objects.filter(user__isnull=False, time_lead=now_localtime)
    email_list = []
    for habit in habits:
        email_list.append(habit.user.email)
    if email_list:
        send_inform_habit(email_list)

