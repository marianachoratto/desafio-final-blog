from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
from blog.forms import ComentarioForm

# View da página inicial 
def index_html(request):
    posts = Post.objects.all() #o valor de posts é uma lista de objetos
    return render(request, 'post_preview.html', {'posts1': posts}) #você pega o valor da chave no HTML 


def resenha_do_livro(request):
    posts = Post.objects.get(pk=2) #aqui tbm é uma lista de objetos, que traz só 1 item
    form = ComentarioForm()
    # print({'posts': posts})
    context = {
        'posts': posts,
        'form': form
    }
    return render(request, 'post1.html', context)

# def comentario(request):
#     form = ComentarioForm()
#     return render(request, 'post1.html', {'form': form} )
