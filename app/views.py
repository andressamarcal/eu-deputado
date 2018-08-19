from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.generic import TemplateView
import requests

class HomeView(TemplateView):
    template_name = "index.html"

class ProposicoesView(TemplateView):
    template_name = ''

    def get(self, request):
        response = requests.get('https://dadosabertos.camara.leg.br/api/v2/proposicoes')
        proposicoes = response.json()
        return render(request, 'proposicoes.html', {
            'id' : proposicoes['id'],
            'ano': proposicoes['ano'],
    })
