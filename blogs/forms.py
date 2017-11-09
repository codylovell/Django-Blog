from django import forms

from blogs.models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text']
        labels = {'title': 'Title', 'text': 'Post'}
        widgets = {'text': forms.Textarea(attrs={'cols': 50})}