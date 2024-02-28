from django.db import models


class Company(models.Model):
    """
    Модель Company представляет собой компанию в иерархии сети по продаже электроники.
    Она может быть заводом, розничной сетью или индивидуальным предпринимателем.

    Attributes:
        name (str): Название компании.
        company_type (int): Тип компании (завод, розничная сеть, индивидуальный предприниматель).
        email (EmailField): Контактный email компании.
        country (str): Страна расположения.
        city (str): Город расположения.
        street (str): Улица расположения.
        house_number (str): Номер дома.
        supplier (ForeignKey): Ссылка на поставщика компании (другую компанию).
        debt (DecimalField): Задолженность перед поставщиком.
        created_at (DateTimeField): Дата и время создания записи.
    """

    FACTORY = 0
    RETAIL_NETWORK = 1
    INDIVIDUAL_ENTREPRENEUR = 2
    COMPANY_TYPES = [
        (FACTORY, "Factory"),
        (RETAIL_NETWORK, "Retail Network"),
        (INDIVIDUAL_ENTREPRENEUR, "Individual Entrepreneur"),
    ]

    name = models.CharField(max_length=255)
    company_type = models.IntegerField(choices=COMPANY_TYPES)
    email = models.EmailField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=20)
    supplier = models.ForeignKey(
        "self", on_delete=models.SET_NULL, null=True, blank=True, related_name="clients"
    )
    debt = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Возвращает строковое представление объекта Company, содержащее его название.
        """
        return self.name

    @property
    def hierarchy_level(self):
        """
        Определяет и возвращает уровень иерархии компании.

        Заводы всегда находятся на 0 уровне. Для розничных сетей и индивидуальных предпринимателей уровень иерархии
        зависит от типа их поставщика. Если поставщик не указан, уровень считается максимальным.

        Returns:
            int: Уровень иерархии компании.
        """
        # Завод всегда находится на 0 уровне
        if self.company_type == self.FACTORY:
            return 0

        # Если поставщик не указан, считаем уровень максимальным
        if not self.supplier:
            return max(self.RETAIL_NETWORK, self.INDIVIDUAL_ENTREPRENEUR)

        # В противном случае определяем уровень на основе поставщика
        return self.supplier.hierarchy_level + 1


class Product(models.Model):
    """
    Модель Product представляет собой продукт, который продается компанией.

    Attributes:
        name (str): Название продукта.
        model (str): Модель продукта.
        release_date (DateField): Дата выхода продукта на рынок.
        company (ForeignKey): Ссылка на компанию, которая предлагает этот продукт.
    """

    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    release_date = models.DateField()
    company = models.ForeignKey(
        Company, related_name="products", on_delete=models.CASCADE
    )

    def __str__(self):
        """
        Возвращает строковое представление объекта Product, включающее название и модель продукта.
        """
        return f"{self.name} ({self.model})"
