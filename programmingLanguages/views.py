from datetime import datetime

import django.core.handlers.wsgi
from django.core.cache import cache
import django.urls
import django.db.models
from django.contrib.auth import logout, login
from django.shortcuts import render, redirect, get_object_or_404
from django.http import *
from django.template import loader, RequestContext
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView

import programmingLanguages.models
from .forms import *
from .models import *
from .serializers import LanguageSerializer
from .utils import DataMixin

from rest_framework import generics


class LanguageAPIView(generics.ListAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class PostHome(DataMixin, ListView):
    model = Post
    template_name = 'programmingLanguages/main.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        mixinContext = self.get_user_context(title='Главная страница',
                                             text=Post.objects.get(title='Главная страница').text)
        return dict(list(context.items()) + list(mixinContext.items()))


class PostAbout(DataMixin, ListView):
    model = Post
    template_name = 'programmingLanguages/main.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        mixinContext = self.get_user_context(title='О языках',
                                             text=Post.objects.get(title='О языках').text)
        return dict(list(context.items()) + list(mixinContext.items()))


class SearchResult(DataMixin, ListView):
    paginate_by = 3
    model = Language
    template_name = 'programmingLanguages/descriptions.html'

    def get_queryset(self):
        return Language.objects.filter(title__icontains=self.request.GET.get('search'))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        mixinContext = self.get_user_context(title='Результаты поиска',
                                             search=self.request.GET.get('search'))

        return dict(list(context.items()) + list(mixinContext.items()))


class LanguageInSubCategoryShow(DataMixin, ListView):
    paginate_by = 3
    model = Language
    template_name = 'programmingLanguages/descriptions.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = get_object_or_404(SubCategory, slug=self.kwargs['subcat'])
        mixinContext = self.get_user_context(title='Список языков в подкатегории',
                                             currentCat=cat)
        return dict(list(context.items()) + list(mixinContext.items()))

    def get_queryset(self):
        return Language.objects.filter(subcategories__slug=self.kwargs['subcat']).prefetch_related('subcategories')


class LanguageInfoShow(DataMixin, DetailView):
    model = Language
    template_name = 'programmingLanguages/main.html'
    slug_url_kwarg = 'idx'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        language = get_object_or_404(Language, slug=self.kwargs['idx'])
        subcat = SubCategory.objects.filter(language=int(language.pk)).select_related('cat')
        mixinContext = self.get_user_context(title=language.title,
                                             text=language.content,
                                             icon=language.icon,
                                             subcat=subcat)
        return dict(list(context.items()) + list(mixinContext.items()))


def page_not_found(request, exception=None):
    #return HttpResponseRedirect(redirect_to='../../../error')
    return render(request, 'programmingLanguages/error404.html')


def error(request: django.core.handlers.wsgi.WSGIRequest):
    return render(request, 'programmingLanguages/error404.html')


class AddLanguagePost(LoginRequiredMixin, DataMixin, CreateView):

    form_class = AddLanguagePost
    template_name = 'programmingLanguages/addLang.html'
    login_url = 'login'

    def form_valid(self, form):
        form.save()
        cache.clear()
        language_object = Language.objects.get(title=form.cleaned_data.get('title'))
        try:
            Language.objects.get(slug=form.cleaned_data.get('slug'))
        except programmingLanguages.models.Language.DoesNotExist:
            try:
                language_object.slug = slugify(language_object.title)
                language_object.save()
            except:
                date = datetime.today().strftime('%d-%m-%Y-%H-%M-%S_')
                language_object.slug = f'{date}{slugify(language_object.title)}'
                language_object.save()
        return redirect(f'show_language_info/{language_object.slug}/')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mixinContext = self.get_user_context(title='Добавить язык',
                                             text='',
                                             button='Добавить')
        return dict(list(context.items()) + list(mixinContext.items()))


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'programmingLanguages/addLang.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mixinContext = self.get_user_context(title='Регистрация',
                                             button='Регистрация')
        return dict(list(context.items()) + list(mixinContext.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('main')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'programmingLanguages/addLang.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mixinContext = self.get_user_context(title='Авторизация',
                                             button='Войти')
        return dict(list(context.items()) + list(mixinContext.items()))

    def get_success_url(self):
        return reverse_lazy('main')


def logout_user(request):
    logout(request)
    return redirect('login')


class Statics(DataMixin, TemplateView):
    template_name = 'programmingLanguages/iframe.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        date = datetime.today().strftime('%d.%m.%y')
        mixinContext = self.get_user_context(title=f'Актуальный рейтинг языков на {date}')
        return dict(list(context.items()) + list(mixinContext.items()))
