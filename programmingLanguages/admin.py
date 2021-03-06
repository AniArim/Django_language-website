from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *
from django import forms
from ckeditor.fields import RichTextFormField


class LanguageAdminForm(forms.ModelForm):
    content = RichTextFormField()

    class Meta:
        model = Language
        fields = '__all__'


class PostAdminForm(forms.ModelForm):
    text = RichTextFormField()

    class Meta:
        model = Post
        fields = '__all__'


class LanguageAdmin(admin.ModelAdmin):
    form = LanguageAdminForm
    list_display = ('title', 'id', 'get_html_logo', 'slug', 'display_subcategory')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('subcategories',)
    prepopulated_fields = {'slug': ('title',)}
    fields = ('title', 'slug', 'icon', 'get_html_logo', 'content', 'subcategories')
    readonly_fields = ('get_html_logo',)
    save_on_top = True

    def get_html_logo(self, language):
        if language.icon:
            return mark_safe(f"<img src='{language.icon.url}' width=70")

    get_html_logo.short_description = 'Логотип'


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'cat_id', 'slug')
    list_display_links = ('id', 'name', 'cat_id')
    search_fields = ('name', 'id')
    list_filter = ('cat_id',)
    prepopulated_fields = {'slug': ('name',)}


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'id')
    search_fields = ('title', 'text', 'id')
    form = PostAdminForm


# Register your models here.
admin.site.register(Language, LanguageAdmin)
admin.site.register(Category)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Post, PostAdmin)

admin.site.site_header = 'Админ-панель сайта о языках программирования'
