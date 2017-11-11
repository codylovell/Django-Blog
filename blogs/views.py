from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from blogs.models import BlogPost
from blogs.forms import BlogPostForm

# Create your views here.
def home(request):
    posts = BlogPost.objects.all()
    context = {'posts': posts}
    return render(request, 'home.html', context)

@login_required
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

@login_required
def edit_post(request, post_id):
    """Edit an exisiting post."""
    #get post to edit.
    if form.is_valid():
        post = BlogPost.objects.get(id=post_id)
        if post.poster != request.user:
            raise Http404

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
