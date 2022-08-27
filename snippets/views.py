from django.shortcuts import render, get_object_or_404, redirect
from .models import Snippet

# Create your views here.


def list_snippet(request):
    snippets = Snippet.objects.all()
    return render(request, 'snippets/list_snippet.html', {'snippets': snippets})


def detail_snippet(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    return render(request, 'snippets/detail_snippet.html', {"snippet": snippet})
