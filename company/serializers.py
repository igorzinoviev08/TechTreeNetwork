from rest_framework import serializers
from .models import Company


class CompanySerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Company.

    Сериализует данные модели Company для использования в API. Включает все поля модели.
    Поле 'debt' установлено как доступное только для чтения, что предотвращает его изменение через API.
    """

    class Meta:
        model = Company  # Указывает модель, которую сериализует данный класс
        fields = "__all__"  # Все поля модели включены в сериализацию
        read_only_fields = ("debt",)  # 'debt' доступно только для чтения
