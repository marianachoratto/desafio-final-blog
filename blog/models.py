from django.db import models

# Create your models here.
class Post(models.Model): 
    nota_livro = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    )
    titulo= models.CharField(blank=False, max_length=100, null=False )
    autor= models.CharField(blank=False, max_length=70, null=False ) 
    date= models.DateTimeField(auto_now_add=True)
    preview= models.TextField(blank=False, max_length=200, null=False)

    nota = models.IntegerField(blank=True, choices=nota_livro)
    content = models.TextField(blank=False, null=False)
    imagem = models.ImageField(upload_to="imagem/", blank=True, null=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"{self.titulo} - {self.autor} - {self.nota}"


class Comentario(models.Model):
    usuario = models.CharField(max_length=50, blank=True)
    comentario = models.TextField(blank=False, max_length=200)
    data2 = models.DateTimeField(auto_now_add=True)
    id_livro = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Comentário de {self.usuario}"

