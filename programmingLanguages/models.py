from datetime import datetime

from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.core.cache import cache


class Language(models.Model):
    title = models.CharField(max_length=255, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, null=True, verbose_name='URL')
    content = RichTextField(blank=True, verbose_name='Текст', config_name='awesome_ckeditor')
    icon = models.ImageField(upload_to='media', null=True, verbose_name='Изображение')
    subcategories = models.ManyToManyField('SubCategory', verbose_name='Категории')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        cache.clear()
        return reverse('show_language_info', kwargs={'idx': self.slug})

    def display_subcategory(self):
        """
        Creates a string for the SubCategory. This is required to display subcategories in Admin.
        """
        return ';  '.join([subcategories.name for subcategories in self.subcategories.all()[:3]])

    display_subcategory.short_description = 'Подкатегории'

    '''def save(self, *args, **kwargs):

        if not self.id:
            super(Language, self).save(*args, **kwargs)

        if not self.slug:
            try:
                self.slug = slugify(self.title)
                super(Language, self).save(*args, **kwargs)
            except:
                date = datetime.today().strftime('%d-%m-%Y-%H-%M-%S_')
                self.slug = f'{date}{slugify(self.title)}'
                super(Language, self).save(*args, **kwargs)'''

    class Meta:
        verbose_name = 'Язык программирования'
        verbose_name_plural = 'Языки программирования'
        ordering = ['title']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Главная категория'
        verbose_name_plural = 'Главные категории'
        ordering = ['name']


class SubCategory(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Название категории')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Главная категория')
    slug = models.SlugField(max_length=100, unique=True, null=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('subcategory', kwargs={'subcat': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['cat_id']


class Post(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='Заголовок')
    text = models.TextField(default='Введите текст статьи', verbose_name='Статья', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['title']

