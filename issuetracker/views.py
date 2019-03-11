from django.shortcuts import render,HttpResponse


# Create your views here.
# Create your views here.
#def say_hello(request):
 #   return HttpResponse("Hello World")
    
# Create your views here.
def get_issues_list(request):
    return render(request, "issues_list.html")    