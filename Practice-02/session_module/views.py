from django.shortcuts import render,redirect

# Create your views here.
def set_name(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        request.session['name'] = name
        return redirect('preference')
    return render(request, 'set_name.html',{})

def set_preference(request):
    if request.method == 'POST':
        fruit = request.POST.get('fruit')
        vegetable = request.POST.get('vegetable')
        movie = request.POST.get('movie')
        preferences = {'fruit':fruit,'vegetable':vegetable,'movie':movie}
        request.session['preferences'] = preferences
        request.session['flag'] = True
        return redirect('display')
    return render(request, 'preference.html',{})

def display(request): 
    users_data = request.session.get('users_data',[])
    # name = request.session.get('preferences','')
    # user_data = {'name':request.session.get('name',''),'preferences':request.session.get('preferences',{})}
    # users_data.append(user_data)
    # request.session['users_data'] = users_data 
    if request.session.get('flag'):
        user_data = {'name':request.session.get('name',''),'preferences':request.session.get('preferences',{})}
        users_data.append(user_data)
        request.session['users_data'] = users_data  
        request.session['flag'] = False        
    return render(request, 'display.html',{"users_data": users_data})

def clear_session(request):
    request.session.clear()
    return redirect('set_name')

