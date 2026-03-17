from django.db import models


class Categoria(models.Model):
    descricao = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'({self.id}) - {self.descricao}'

# alexa prepara lata monstre
# ok chefi
# alexa abrir lata monstre
# ok chefi
# alexa obrigado pera lrata
# denada chefi
