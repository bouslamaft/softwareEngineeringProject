from django.contrib.admin import register, ModelAdmin, TabularInline

from lms.storage.models import Book, Category, Author, PhysicalBook, PhysicalBookRentHistory


class PhysicalBookInlines(TabularInline):
    model = PhysicalBook
    show_change_link = True


class PhysicalBookHistoryInline(TabularInline):
    model = PhysicalBookRentHistory


@register(Book)
class BookAdmin(ModelAdmin):
    inlines = [PhysicalBookInlines]


@register(PhysicalBook)
class PhysicalBookAdmin(ModelAdmin):
    inlines = [PhysicalBookHistoryInline]


@register(Category)
class CategoryAdmin(ModelAdmin):
    pass


@register(Author)
class AuthorAdmin(ModelAdmin):
    pass
