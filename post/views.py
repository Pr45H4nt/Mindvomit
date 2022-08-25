from django.shortcuts import redirect, render
from .models import Posts
from .models import feedback as f
from .forms import addpost , Feedback
# Create your views here.
def home(request):
    articles = Posts.objects.all().order_by('-id')
    if request.method == "GET":
        qwery = request.GET.get('qwery')
        if qwery != None:
            articles = Posts.objects.filter(title__icontains = qwery)
    data = {
        'articles': articles
    }
    return render(request, "home.html" , data)

def post(request, slug):
    article = Posts.objects.get(slug=slug)
    data = {
        'article': article
    }
    return render(request,'post.html',data)

def adding(request):
    a = ""
    if request.method == "POST":
        title = request.POST['Title']
        content = request.POST['content']
        newpost = Posts(title = title, content = content)
        newpost.save()
        a = "<div class='alert alert-success alert-dismissible fade show'><strong>Success!</strong> Your Post has been submitted. &emsp;<a href='/'><button>Home</button></a><button type='button' class='btn-close' data-bs-dismiss='alert'></button></div>"
    data = {
        'form' : addpost(),
        'message': a
    }
    return render(request, 'adding.html' , data )

def feedback(request):
    if request.method == "POST":
        Name = request.POST.get('Name')
        contact = request.POST.get('contact')
        Email = request.POST.get('Email')
        message = request.POST.get('message')
        newf = f(Name = Name , contact = contact ,Email = Email , message = message )
        newf.save()
        return redirect('home')
    
    data= {
        'form' : Feedback()
    }
    return render(request, 'feedback.html' , data)

def about(request):
    return render(request, "index.html")



    