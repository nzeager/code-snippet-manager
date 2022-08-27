from django.contrib import admin
from .models import User, Snippet, Language, Tag

# Register your models here.
admin.site.register(User)
admin.site.register(Snippet)
admin.site.register(Language)
admin.site.register(Tag)
