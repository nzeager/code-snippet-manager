from django.shortcuts import render, get_object_or_404, redirect
from .models import Snippet, Language, Tag
from .forms import SnippetForm, LanguageForm, TagForm

# Create your views here.

# snippets


def list_snippet(request):
    snippets = Snippet.objects.all()
    return render(request, 'snippets/list_snippet.html', {'snippets': snippets})


def detail_snippet(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    return render(request, 'snippets/detail_snippet.html', {"snippet": snippet, "users": snippet.user.all(), "tags": snippet.tag.all()})


def create_snippet(request):
    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.author = request.user
            snippet.save()
            snippet.user.add(request.user)
            snippet.save()
            return redirect('detail_snippet', pk=snippet.pk)
    else:
        form = SnippetForm()
    return render(request, 'snippets/edit_snippet.html', {'form': form})


def edit_snippet(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    if request.method == "POST":
        form = SnippetForm(request.POST, instance=snippet)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.save()
            return redirect('detail_snippet', pk=snippet.pk)
    else:
        form = SnippetForm(instance=snippet)
    return render(request, 'snippets/edit_snippet.html', {'form': form})


def delete_snippet(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    snippet.delete()
    return redirect('list_snippet')


# languages
def list_language(request):
    languages = Language.objects.all()
    return render(request, 'snippets/list_language.html', {'languages': languages})


def detail_language(request, pk):
    language = get_object_or_404(Language, pk=pk)
    return render(request, 'snippets/detail_language.html', {"language": language})


def create_language(request):
    if request.method == "POST":
        form = LanguageForm(request.POST)
        if form.is_valid():
            language = form.save()
            return redirect('detail_language', pk=language.pk)
    else:
        form = LanguageForm()
    return render(request, 'snippets/edit_language.html', {'form': form})


def edit_language(request, pk):
    language = get_object_or_404(Language, pk=pk)
    if request.method == "POST":
        form = LanguageForm(request.POST, instance=language)
        if form.is_valid():
            language = form.save(commit=False)
            language.save()
            return redirect('detail_language', pk=language.pk)
    else:
        form = LanguageForm(instance=language)
    return render(request, 'snippets/edit_language.html', {'form': form})


def delete_language(request, pk):
    language = get_object_or_404(Language, pk=pk)
    language.delete()
    return redirect('list_language')


# tags
def list_tag(request):
    tags = Tag.objects.all()
    return render(request, 'snippets/list_tag.html', {'tags': tags})


def detail_tag(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    return render(request, 'snippets/detail_tag.html', {"tag": tag})


def create_tag(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            tag = form.save()
            return redirect('detail_tag', pk=tag.pk)
    else:
        form = TagForm()
    return render(request, 'snippets/edit_tag.html', {'form': form})


def edit_tag(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == "POST":
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            tag = form.save(commit=False)
            tag.save()
            return redirect('detail_tag', pk=tag.pk)
    else:
        form = TagForm(instance=tag)
    return render(request, 'snippets/edit_tag.html', {'form': form})


def delete_tag(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    tag.delete()
    return redirect('list_tag')


# user
def user_profile(request):
    snippets = Snippet.objects.filter(user=request.user)
    return render(request, 'snippets/profile.html', {"snippets": snippets})
