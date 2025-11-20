from django.shortcuts import render, get_object_or_404
from .models import Post, Categoria

def blog(request):
    lista_posts = Post.objects.all()
    return render(request, "blog/blog.html", {"posts": lista_posts})

def categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    posts = Post.objects.filter(categorias=categoria)
    return render(request, "blog/categoria.html", {'categoria': categoria, "posts": posts})