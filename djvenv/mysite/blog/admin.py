from django.contrib import admin
from .models import Post

@admin.register(Post)
class ModifiedAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']    # поля которые будут отображаться в админке
    list_filter = ['status', 'created', 'publish', 'author']    # поле фильтрации справа
    search_fields = ['title', 'body']   # добавит панль для поиска сверху
    prepopulated_fields = {'slug': ('title',)}   # при записи в поле значения перекинет запись еще и в поле ключа, в даном случае в из title в slug в ормате slug
    raw_id_fields =  ['author']    #
    autocomplete_fields = ['author']    #
    date_hierarchy = 'publish'    # добавит на верху даты историй публикаций
    ordering = ['status', 'publish']    # определит по каким полям производить сортировку

# Register your models here.
