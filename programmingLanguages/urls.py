from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin
from testsite import settings
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', PostHome.as_view(), name='main'),
    path('show_language_info/<slug:idx>/', LanguageInfoShow.as_view(), name='show_language_info'),
    path('subcategory/<slug:subcat>/', LanguageInSubCategoryShow.as_view(), name='subcategory'),
    path('about', PostAbout.as_view(), name='about'),
    #path('error', error, name='error'),
    path('addLang', AddLanguagePost.as_view(), name='addLang'),
    path('login', LoginUser.as_view(), name='login'),
    path('register', RegisterUser.as_view(), name='register'),
    path('logout', logout_user, name='logout'),
    path('search', SearchResult.as_view(), name='search'),
    path('statics', Statics.as_view(), name='statics'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




