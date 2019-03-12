from django.shortcuts import render,HttpResponse, redirect
from .models import Issues


# Create your views here.
# Create your views here.
#def say_hello(request):
 #   return HttpResponse("Hello World")
    
# Create your views here.
def get_issues_list(request):
    results = Issues.objects.all()
    return render(request, "issues_list.html" , {'issues':results}) #dic key is issues value is results   
    
def create_an_issue(request):
    if request.method=="POST":
        new_issue = Issues()
        new_issue.done = 'done'in request.POST
        new_issue.name= request.POST.get('name')
        
        return redirect(get_issues_list)
    return render(request, "issue_form.html")