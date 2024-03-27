from django import forms
# from blog.models import Comentario

class ComentarioForm(forms.Form):
    # class Meta: 
    #     model = Comentario
    #     fields= ['usuario', 'comentario']
    nome_login = forms.CharField(
        label = "Nome de Login",
        required = True,
        max_length = 100
    )
    