from django.db.models import Count

from programmingLanguages.models import *
from django.core.cache import cache


class DataMixin:

    def get_user_context(self, **kwargs):
        context = kwargs

        listSubCat = SubCategory.objects.values('name').annotate(total=Count('language')).filter(total__gt=0)
        listSubCat = [i.get('name') for i in listSubCat]

        category = cache.get('category')
        if not category:
            category = Category.objects.all()
            cache.set('category', category, 600)

        subcategory = cache.get('subcategory')
        if not subcategory:
            subcategory = SubCategory.objects.all()
            cache.set('subcategory', subcategory, 600)

        context['category'] = category
        context['subcategory'] = subcategory
        context['listSubCat'] = listSubCat
        return context
