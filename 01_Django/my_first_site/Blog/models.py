from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    '''
        SQL -> CREATE TABLE tbl_Post(
            title Varchar(250),
            ....
            publish DATE DEFAULT = CURRENT_DATE()
            ...
            status varchar(2) check (DF or PB)
            author int foreign key (author) REFERENCES tbl_Authors(author)
        )
        el atributo created sera dado solo cuando se cree un objeto de esta clase
        update sera dado cada que se modifique, debido a eso usamos parametros de auto_now
    '''
    
    #manejo de estados de la publicacion
    class Status(models.TextChoices):
        DRAF = 'DF', 'Draft'
        PUBLISEHD = 'PB', 'Published'

    title   = models.CharField(max_length = 250)
    slug    = models.SlugField(max_length = 250)

    '''
        atributo foraneo (los datos pertenecen a otra entidad)
        objeto, eliminacion, nombre_relativo
    '''
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')

    body    = models.TextField()
    publish = models.DateTimeField(default = timezone.now)
    created = models.DateTimeField(auto_now_add = True)
    update  = models.DateTimeField(auto_now = True)
    
    #Atributo para el estado, seran seleccionables entre los dos estados Draf, published...
    status = models.CharField( max_length=2,
                              choices = Status.choices,
                              default = Status.DRAF)

    '''
        Meta clase - subclase para controlar ordenamiento e indexacion de la clase principal
        ordening : forma en la que se ordenaran los datos ('-' : invertido)
        indexes : indexacion a travez del campo publis para mejorar la consulta al accedes a un Post
    '''
    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish'])
        ]

    # obtendremos el titulo cuando se haga un print de la clase
    def __str__(self):
        return self.title