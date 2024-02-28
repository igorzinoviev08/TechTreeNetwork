from rest_framework import viewsets, filters
from .models import Company
from .permissions import IsActiveEmployee
from .serializers import CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    """
    ViewSet для обработки запросов к модели Company.

    Предоставляет операции CRUD для модели Company. Включает поиск по стране и ограничение
    на обновление поля 'debt'.
    """

    queryset = Company.objects.all()  # Получаем все объекты Company
    serializer_class = CompanySerializer  # Указываем используемый сериализатор
    permission_classes = [IsActiveEmployee]  # Доступ только для активных сотрудников
    filter_backends = [filters.SearchFilter]  # Включаем возможность поиска
    search_fields = ["country"]  # Поля для поиска

    def perform_update(self, serializer):
        """
        Обрабатывает операцию обновления для объекта Company.

        При обновлении объекта 'debt' не изменяется и сохраняет свое первоначальное значение.
        """
        # Сохраняем объект, не позволяя изменять значение 'debt'
        serializer.save(debt=self.get_object().debt)
