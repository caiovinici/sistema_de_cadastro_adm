from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.utils.safestring import mark_safe # informando que string é segura para o navegador
# criando tabela no BD

# class Empresas(models.Model):
#     #CharField campo de texto / max_length= capacidade de caracteres
#     nome = models.CharField(max_length=50)
#     cnpj = models.CharField(max_length=30)
#     #
#     site = models.URLField() # campo para URL do site 
#     data_final_captacao = models.DateField() # 



class Empresas(models.Model):
    tempo_existencia_choices = ( # *
    ('-6', 'Menos de 6 meses'),
    ('+6', 'Mais de 6 meses'),
    ('+1', 'Mais de 1 ano'),
    ('+5', 'Mais de 5 anos')
 
 )
#    
    estagio_choices = (
    ('I', 'Tenho apenas uma idea'),
    ('MVP', 'Possuo um MVP'),
    ('MVPP', 'Possuo um MVP com clientes pagantes'),
    ('E', 'Empresa pronta para escalar'),
 )
#
    area_choices = (
    ('ED', 'Ed-tech'),
    ('FT', 'Fintech'),
    ('AT', 'Agrotech'),
 
 )
#
    # campo de relacionamento com a tabela usuario /
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    
    nome = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=30)
    site = models.URLField()
    
    tempo_existencia = models.CharField(max_length=2, choices=tempo_existencia_choices, default='-6')
    
    #TexteField = sem limitação de caracteres
    descricao = models.TextField()
    
    data_final_captacao = models.DateField()
    percentual_equity = models.IntegerField() # Percentual esperado
    estagio = models.CharField(max_length=4, choices=estagio_choices, default='I')
    area = models.CharField(max_length=3, choices=area_choices)
    publico_alvo = models.CharField(max_length=3)
    valor = models.DecimalField(max_digits=9, decimal_places=2) # Valor total a ser vendido
    
    # aonde faz upload de arquivos
    pitch = models.FileField(upload_to='pitchs') # criando pasta pitchs dentro da pasta media
    logo = models.FileField(upload_to='logo')
    #
    def __str__(self):
        return f'{self.user.username} | {self.nome}'
    #
    @property # faz com que a func funcione como uma propriedade
    def status(self):
        if date.today() > self.data_final_captacao:
            return mark_safe('<span class="badge text-bg-success">Captação finalizada</span>')
    
        return mark_safe('<span class="badge text-bg-primary">Em captação</span>')
