from django.shortcuts import render,HttpResponse, redirect,get_object_or_404
from .models import Issues
from .forms import IssuesForm


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
        form = IssuesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(get_issues_list)
            
    else:
        form=IssuesForm()
    return render(request, "issue_form.html", {'form':form})
    

def edit_an_issues(request, id ):
    issues = get_object_or_404(Issues, pk=id)
    
    if request.method=="POST":
       form = IssuesForm(request.POST,instance=issues)
       if form.is_valid():
           form.save()
       return redirect(get_issues_list) 
    else:    
        form = IssuesForm(instance=issues) 
        
    return render(request, "issue_form.html", {'form':form})
    
def  toggle_status(request,id):
     issues = get_object_or_404(Issues, pk=id)
     issues.done = not issues.done 
     issues.save()
     return redirect(get_issues_list)     