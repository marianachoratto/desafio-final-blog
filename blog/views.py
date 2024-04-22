from django.shortcuts import render, redirect
from blog.models import Post, Comentario
from blog.forms import ComentarioForm, CadastroForm, CadastroUsuarioForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib import messages



# View da página inicial
def index_html(request):
    posts = Post.objects.all()  # o valor de posts é uma lista de objetos
    return render(
        request, "preview_livros.html", {"posts1": posts}
    )  # você pega o valor da chave no HTML


# View do conteúdos total das páginas com resenhas. Ela pega o livro, o comentário, o id do livro e o formulário de comentário
def resenha_do_livro(request, id):
    id_do_livro = id
    posts = Post.objects.get(
        pk=id
    )  # aqui tbm é uma lista de objetos, que traz só 1 item
    comentarios = Comentario.objects.order_by("-data2").filter(id_livro_id=id)
    sucesso = False
    form = ComentarioForm()
    fotografia = fotografia = get_object_or_404(Post, pk=id)
    dataToBePassed = {
        "posts": posts,
        "form": form,
        "sucesso": sucesso,
        "id_do_livro": id_do_livro,
        "comentarios": comentarios,
        "fotografia": fotografia, 
    }
    if request.method == "GET":
        return get_resenha(request, dataToBePassed)
    elif request.method == "POST":
        return post_resenha(request, dataToBePassed)


# view da resenha do livro (função chamada acima)
def get_resenha(request, dataToBePassed):
    return render(request, "resenha_de_livro.html", dataToBePassed)


# view do formulário de comentários (função chamada acima)
def post_resenha(request, dataToBePassed):
    form = ComentarioForm(request.POST)
    if form.is_valid():
        dataToBePassed["sucesso"] = True
        post_instance = Post.objects.get(id=dataToBePassed["id_do_livro"])

        new_comment = Comentario(
            usuario=form["usuario"].value(),
            comentario=form["comentario"].value(),
            id_livro=post_instance,
        )
        new_comment.save()

        return render(request, "resenha_de_livro.html", dataToBePassed)


# view da barra de pesquisa
def pesquisar_livro(request):
    if request.method == "GET":
        try:
            pesquisa = request.GET.get("pesquisa", None)

            if type(pesquisa) == str or None:

               consulta = Post.objects.filter(titulo__icontains=pesquisa) | \
                    Post.objects.filter(autor__icontains=pesquisa) | \
                    Post.objects.filter(content__icontains=pesquisa)
            return render(request, "preview_livros.html",{"posts1": consulta, 'pesquisa': pesquisa, 'consulta':consulta})
        except ValueError:
            consulta = Post.objects.all()
            return render(request, "preview_livros.html", {"posts1": consulta, 'pesquisa': pesquisa, 'consulta':consulta})

#cadastrar livro novo no banco de dados
def realizar_cadastro_de_livro(request): 
    if request.user.is_authenticated:
        sucesso = False
        if request.method == "GET":
            form = CadastroForm()
        else:
            form = CadastroForm(request.POST, request.FILES)
            if form.is_valid():
                sucesso = True
                form.save()
                livros = Post.objects.all()
                return render(request, "tabela_de_livros.html",{"livros": livros})
        contexto = {"form": form, "sucesso": sucesso}
        return render(request, "cadastro_de_livros.html", contexto)

#tabela de livros cadastrados
def tabela_de_livros(request):
    print('PASSEI AQI', request.user.is_authenticated )
    if request.user.is_authenticated:
        print('TABELA DE LIVROS')
        if request.method == "GET":
            livros = Post.objects.all()
        return render(request, "tabela_de_livros.html", {"livros": livros})

#botão de excluir
def excluir(request, id):
    excluir_livro = get_object_or_404(Post, pk=id)
    excluir_livro.delete()

    if request.method == "GET":
        livros = Post.objects.all()
    return render(request, "tabela_de_livros.html", {"livros": livros} )

#página de edição de um livro individual
def editar_um_livro(request, id):
    if request.user.is_authenticated:
        if request.method == "GET":
            livro = Post.objects.get(pk=id)
            form = CadastroForm(instance=livro)
            return render(request, "editar_um_livro.html", {"livro": livro, 'form':form})
        elif request.method == "POST":
            sucesso = False 
            form = CadastroForm(request.POST, request.FILES)
            livro = Post.objects.get(pk=id)
            livro.titulo = form['titulo'].value()
            livro.nota = form['nota'].value()
            livro.autor = form['autor'].value()
            livro.preview = form['preview'].value()
            livro.content = form['content'].value()
            livro.imagem = request.FILES['imagem']
            livro.save()
            form = CadastroForm(request.POST, instance=livro)
            sucesso = True
            livro = Post.objects.get(pk=id)
            contexto= {
                "sucesso": sucesso,
                "form":form,
                "livro": livro
            }
            form = CadastroForm(instance=livro)
            return render(request, "editar_um_livro.html", contexto)
        
# Reportando problemas de ediçao
def report_problem(request):
    if request.method == 'POST':
        # Exibindo a mensagem de sucesso
        messages.success(request, 'O problema foi reportado com sucesso!')
        return redirect("index")
    else:
        return render(request,"report_problem.html")


#página de login/cadastro 
def cadastrar(request):
    form= CadastroUsuarioForm()
    login_form = AuthenticationForm()
    erro = False
    sucesso= False
    if request.method == 'POST':
        form= CadastroUsuarioForm(request.POST)
        if form.is_valid() and not User.objects.filter(username=form['username'].value()).exists():
            User.objects.create_user(
                username=form['username'].value(),
                password=form['password'].value(),
                email=form['email'].value()
            )
            sucesso= True
            erro = False
            return render(request, "cadastro_usuario.html", {"form": form, "login_form": login_form, "erro": erro, "sucesso": sucesso})
        else: 
            form = CadastroUsuarioForm()
            erro = True
    return render(request, "cadastro_usuario.html", {"form": form, "login_form": login_form, "erro": erro, "sucesso": sucesso})


def fazer_login(request):
    erro = False
    if request.method == "POST":
        login_form= AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("editar_livros")
        else:
            login_form= AuthenticationForm()
            form= CadastroUsuarioForm()
            erro_login = True
            return render(request, "cadastro_usuario.html", {"erro_login": erro_login, "login_form": login_form, "form": form})

def logoff(request):
    auth.logout(request)
    return redirect("cadastro")