from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse

from .models import Company, Product


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    """
    Администраторская панель для модели Company.
    """

    list_display = (
        "name",
        "email",
        "country",
        "city",
        "view_supplier_link",
        "debt",
        "created_at",
    )
    list_filter = ("city",)
    search_fields = ("name", "city")
    actions = ["clear_debt"]

    def view_supplier_link(self, obj):
        """
        Создает HTML-ссылку на страницу редактирования поставщика.

        Args:
            obj (Company): Экземпляр модели Company.

        Returns:
            str: HTML-ссылка на страницу поставщика или '-' если поставщик отсутствует.
        """
        if obj.supplier:
            url = reverse("admin:company_company_change", args=[obj.supplier.pk])
            return format_html('<a href="{}">{}</a>', url, obj.supplier.name)
        return "-"

    view_supplier_link.short_description = "Поставщик"

    def clear_debt(self, request, queryset):
        """
        Действие для обнуления задолженности выбранных компаний.

        Args:
            request: HTTP-запрос.
            queryset: QuerySet выбранных объектов.
        """
        queryset.update(debt=0)

    clear_debt.short_description = "Очистить задолженность"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Администраторская панель для модели Product.
    """

    list_display = ("name", "model", "release_date", "company")
    list_filter = ("company",)
    search_fields = ("name", "model")
