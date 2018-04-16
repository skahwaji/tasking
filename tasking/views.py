from django.shortcuts import render


#another comment
def welcome(request):
    return render(request, "tasking/index.html")