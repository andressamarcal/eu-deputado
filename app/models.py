from django.db import models


class Proposicoes(models.Model):

    id                      = models.IntegerField(primary_key=True)
    siglaTipo               = models.TextField()
    numero                  = models.IntegerField()
    ano                     = models.IntegerField()
    idAutor                 = models.IntegerField()
    autor                   = models.TextField()
    siglaPartidoAutor       = models.TextField()
    idPartidoAutor          = models.IntegerField()
    siglaUfAutor            = models.TextField()
    keywords                = models.TextField()
    tramitacaoSenado        = models.BooleanField()
    dataInicio              = models.DateField()
    dataFim                 = models.DateField()
    dataApresentacaoInicio  = models.DateField()
    dataApresentacaoFim     = models.DateField()
    idSituacao              = models.IntegerField()
    pagina                  = models.IntegerField()
    itens                   = models.IntegerField()
    ordem                   = models.TextField()
    ordenarPor              = models.TextField()
