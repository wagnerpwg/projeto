from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Post(models.Model):
    Titulo = models.CharField(max_length=300)
    Resumo = RichTextField()
    Conteudo = RichTextUploadingField()
    Autor = models.ForeignKey(User, on_delete=models.PROTECT)
    Data = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.Titulo
    