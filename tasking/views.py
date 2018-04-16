from django.shortcuts import render


#add some changes to test git
def welcome(request):
    return render(request, "tasking/index.html")