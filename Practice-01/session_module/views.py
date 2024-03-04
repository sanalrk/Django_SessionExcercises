from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html',{})

def initialise(request):
    request.session['counter'] = 0
    return render(request,'initialise.html',{})

def increment(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    else:
        request.session['counter'] += 1

    return render(request,'increment.html',{})

def show(request):
    counter = request.session.get('counter',0)
    return render(request,'show.html',{"counter": counter})