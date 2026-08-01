from django.shortcuts import render, redirect
from .models import Post
from .forms import Postform
from django.contrib.auth import logout














posts = [   {
        "title": "Looking for a Baby Stroller Recommendation",
        "content": "Hi everyone! My baby is about 8 months old, and I'm looking for a durable stroller that's lightweight and easy to fold. My budget is around ₦120,000. If you've used one that you can recommend, I'd really appreciate your suggestions and where you bought it. Thanks!"
    },
    {
        "title": "Birthday Gift Ideas for My Wife",
        "content": "My wife's birthday is coming up next month, and I'd love to surprise her with something thoughtful. She enjoys reading, skincare, and occasional weekend getaways. My budget is ₦150,000. Any unique gift ideas or experiences you've tried?"
    },
    {
        "title": "Affordable Home Office Setup",
        "content": "I'm setting up a small home office and need recommendations for a comfortable chair, a sturdy desk, and good lighting. My total budget is about ₦250,000. If you've recently built your workspace, please share your experience."
    }
]
    














# Create your views her
def all_posts(request): 
    posts = Post.objects.all().order_by('-created_at') # 
    return render(request, 'posts.html',{"posts":posts}) 


def create_post(request):
    if request.method == "POST":
        form = Postform (request.POST, request. FILES)
        if form.is_valid():
            form.save()
            return redirect('/posts')
        else:
            print(form.errors)
        
    else:
        form = Postform()
    return render(request, 'create_post.html', {"form": form})

def single_post(request, id):
    post = Post.objects.get(id=id)

    return render(request, 'single_post.html', {'post': post})


def edit_post(request, id):
    post = Post.objects.get(id=id)

    if request.method == "POST":
        form = Postform(request.POST, request. FILES, instance=post)
            
        if form.is_valid():
            form.save()
            return redirect('/posts')
            
    else:
        form = Postform(instance=post)
    return render(request, 'edit_post.html', {"form": form, 'post': post})

def single_post(request, id):
    post = Post.objects.get(id=id)

    return render(request, 'single_post.html', {'post': post})



def delete_post(request, id):
    post = Post.objects.get(id=id)

    if request.method == "POST":
        post.delete()


    return redirect("/posts")

def logout(request):
    logout(request)
    return redirect('/posts')

def login(request):
    login(request)
    return redirect('/posts')


def profile(request):
    profile = Post.objects.get(user=request.user)
    return render(request, "profile.html", {"profile": profile})
