from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def sign(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()            
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'logapp/signup.html',{'form': form})

@login_required
def counter(request):
     
     visits = request.session.get('visits',0)
     visits +=1
     request.session['visits']= visits
     return render(request,'logapp/counter.html', {'visits': visits})


            