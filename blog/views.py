from django.shortcuts import render
from django.http import HttpResponse

# View da página inicial 
def index_html(request):
    return render(request, 'index.html')
