from django import template
from testsite.settings import MEDIA_URL

register = template.Library()


@register.simple_tag
def get_logo():
    return MEDIA_URL


@register.simple_tag()
def get_menu():
    menu = [
        {'title': 'Главная страница', 'url_name': 'main'},
        {'title': 'О языках', 'url_name': 'about'},
        {'title': 'Рейтинг', 'url_name': 'statics'},
        {'title': 'Добавить язык', 'url_name': 'addLang'},

    ]
    return menu

