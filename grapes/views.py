from django.shortcuts import render

# Create your views here.
def login(request):
    data="sudheer"
    d={"username":data}
    return render(request,'login.html',context=d)