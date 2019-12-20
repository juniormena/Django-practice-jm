from django.shortcuts import render, get_object_or_404,redirect
from .models import Post,Author
from .forms import PostModelForm
from django.conf import settings
from django.contrib import messages
# Create your views here.
def posts_list(request):
    all_posts = Post.objects.all()
    context={
        'all_posts':all_posts
    }
    print(settings.BASE_DIR)
    return render(request, "posts/posts_list.html",context)

#CRUD

def posts_detail(request, slug):
    unique_post = get_object_or_404(Post,slug=slug)
    context = {
        'post':unique_post
    }
    messages.info(request,'you access to all posts')
    return render(request, "posts/post_detail.html",context)


def post_create(request):
    author,created = Author.objects.get_or_create(user=request.user,email=request.user.email, cellphone = 8495786595)
    form = PostModelForm(request.POST or None, request.FILES or None)#request.FILES para manjear archivo que no sean de texto#
    if form.is_valid():
        form.instance.authors = author
        form.save()
    context = {
        'form':form
    }
    return render(request,"posts/post_create.html",context)


def post_update(request,slug):
    unique_post = get_object_or_404(Post,slug=slug)
    form = PostModelForm(request.POST or None, request.FILES or None, instance=unique_post)
    if form.is_valid():
        form.save()
    context = {
        'form':form
    }
    return render(request, "posts/post_update.html",context)


def post_delete(request,slug):
    unique_post = get_object_or_404(Post,slug=slug)
    unique_post.delete()
    return redirect('/posts/')