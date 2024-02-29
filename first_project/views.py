from django.shortcuts import render
def home(request):
    # return HttpResponse("hi")
    return render(request,'base.html')