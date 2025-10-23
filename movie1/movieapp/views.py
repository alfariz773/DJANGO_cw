from django.shortcuts import render
from.form import movieform
from.models import moviefan
def movies(request):
    if request.method == 'POST':
        form = movieform(request.POST)
        if form.is_valid():
            cust = moviefan()
            cust.movie = form.cleaned_data['movie']
            cust.year = form.cleaned_data['year']
            cust.save()
            return render(request,'base.html',{
                'movie':cust.movie,
                'year': cust.year
                
            })
    else:
        form= movieform()
    return render(request,'index.html',{'form':form})
            