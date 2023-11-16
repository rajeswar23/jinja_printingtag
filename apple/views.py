from django.shortcuts import render

# Create your views here.
def sudheer(request):
    data="Hai sudheer i am displaying data"
    d={"display":data}
    return render(request,'sudheer.html',context=d)