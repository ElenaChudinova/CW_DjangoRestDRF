from rest_framework.serializers import ValidationError


class Validator:
    def __init__(self, field):
        self.field = field

    def __call__(self, attrs):
        related_habit = attrs.get("related_habit")
        pleasant_habit_sign = attrs.get("pleasant_habit_sign")
        time_complete = attrs.get("time_complete")
        frequency = attrs.get("frequency")
        reward = attrs.get("reward")

        if related_habit and pleasant_habit_sign:
            raise ValidationError("Привычки не могут быть активны одновременно")
        if time_complete and time_complete > 120:
            raise ValidationError("Время выполнения не должно быть больше 120 минут.")
        if frequency < 1 or frequency > 7:
            raise ValidationError("Периодичность выполнения должна быть от 1 до 7 дней")
        if pleasant_habit_sign and (related_habit or reward):
            raise ValidationError(
                "У приятной привычки не может быть вознаграждения или связанной привычки"
            )
        if related_habit == reward:
            raise ValidationError("У связанной привычки не может быть вознаграждения")

        return attrs
