# Django_language-website
Django 4.0.4 WEB-приложение "Языки программирования". Тестовый проект

Просмотреть сайт: https://shrouded-badlands-34053.herokuapp.com

Для доступа в admin panel с правами только для просмотра: login - testuser, password - gmwMSPxd

Верстка не выполнена, сайт отображается корректно только на ПК.

Вся информация взята из [Википедии](https://ru.wikipedia.org/wiki/Список_языков_программирования_по_категориям#Неполнофункциональные_языки)

Функционал:
- Регистрация и авторизация пользователей на сайте.
- Добавление нового языка доступно только авторизированным пользователям. В противном случае - redirect на страницу авторизации.
- Для добавления нового языка необходимо пройти капчу. 
- После добавления языка редирект на страницу просмотра этого языка.
- Поиск выполняется по названию языка ('title' в базе данных)
- Добавлена пагинация для просмотра списка языков по категориям.
- SideBar слева заполняется автоматически из базы данных.

Для редактирования текста используется CkEditor, для кеширования - django.core.cache. Добавлен Django Debug Toolbar. В таблицах базы данных используются связи ForeignKey, ManyToMany. Добавлены стили Bootstrap. Для select box добавлен Select2. Рейтинг отображается через iframe с сайта [Tiob](https://www.tiobe.com/tiobe-index/)

![alt tag](https://github.com/AniArim/images/blob/main/testsite/main.png)

