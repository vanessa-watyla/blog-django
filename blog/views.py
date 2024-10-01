from django.shortcuts import render, redirect
from django.contrib import messages


from .models import Post, Comentario
from django.http import HttpResponse
from datetime import datetime

def index(request):
    post = Post.objects.all()
    context = {
        'post_template': post,
    }
    return render(request, "index.html", context)

def detalhe(request, id_post):
    if request.method == 'POST':
        publicacao = request.POST
        
        
        comentario_texto = publicacao.get('comentario_texto')
        if comentario_texto:
      
            Comentario.objects.create(
                post_id=Post.objects.get(id=id_post),
                texto=comentario_texto,
                com_date=datetime.now()
            )
            messages.success(request, 'Comentário adicionado com sucesso.')
        else:
            messages.error(request, 'O comentário não pode estar vazio.')
        
        return redirect('index')

    
    post = Post.objects.get(id=id_post)
    comentario = Comentario.objects.filter(post_id=id_post)
    
   
    context = {
        'post_template': post,
        'opcoes_template': comentario
    }
    
    return render(request, "detalhe.html", context)

