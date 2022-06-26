from rest_framework import serializers
from .models import *


class LanguageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Language
		fields = ('title', 'id', 'slug', 'subcategories')
