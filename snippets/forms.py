from django import forms
from .models import Snippet, Language, Tag


class SnippetForm(forms.ModelForm):

    class Meta:
        model = Snippet
        fields = ('title', 'description', 'code', 'language', 'user', 'tag')


class LanguageForm(forms.ModelForm):

    class Meta:
        model = Language
        fields = ('name', 'version')


class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = ('name',)
