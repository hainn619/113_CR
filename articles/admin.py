from django.contrib import admin
from .models import Section, Article, ArticleType, Status

admin.site.register([Article, Section, ArticleType, Status])
