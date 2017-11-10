from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from blogs.models import BlogPost
from blogs.forms import BlogPostForm

# Create your views here.
def home(request):
    posts = BlogPost.objects.all()
    context = {'posts': posts}
    return render(request, 'home.html', context)

def new_post(request):
    """Add a new post."""
    if request.method != 'POST':
        form = BlogPostForm()
    else:
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))

    context = {'form': form}
    return render(request, 'new_post.html', context)

def edit_post(request, post_id):
    """Edit an exisiting post."""
    #get post to edit.
    if form.is_valid():
        post = BlogPost.objects.get(id=post_id)

        #get text of post
        text = post.text
    if request.method != 'POST':
        form = BlogPostForm(instance=post)

    else:
        form = BlogPostForm(instance=post, data=request.POST)
        form.save()
        return HttpResponseRedirect(reverse('home'))

    context = {'post': post, 'text': text, 'form': form}
    return render(request, 'edit_post.html', context)
