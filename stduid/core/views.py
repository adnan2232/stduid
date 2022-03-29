from django.shortcuts import render

# Create your views here.
def homepage(req):
    return render(req, 'index.html')

def tempPage(req):
    return render(req, 'temp.html')
    