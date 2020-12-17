from django.db import models

class Base(models.Model):
    creation = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Curso(Base):
    title = models.CharField(max_length=255)
    url = models.URLField(unique=True)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['id']

    def __str__(self):
        return self.title

class Avaliacao(Base):
    curso = models.ForeignKey(Curso, related_name='avaliacoes', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    comment = models.TextField(blank=True, default='')
    avaliacao = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        unique_together = ['email', 'curso']
        ordering = ['id']

    def __str__(self):
        return f'{self.name} avaliou o curso {self.curso} com nota {self.avaliacao}'