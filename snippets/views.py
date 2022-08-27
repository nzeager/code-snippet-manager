from django.shortcuts import render, get_object_or_404, redirect
from .models import Snippet
from .forms import SnippetForm

# Create your views here.


def list_snippet(request):
    snippets = Snippet.objects.all()
    return render(request, 'snippets/list_snippet.html', {'snippets': snippets})


def detail_snippet(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    return render(request, 'snippets/detail_snippet.html', {"snippet": snippet})


def create_snippet(request):
    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save()
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
