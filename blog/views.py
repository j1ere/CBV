from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import BlogPost

# Create your views here.
class PostListView(ListView):
    model = BlogPost
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/post_detail.html'

class PostCreateView(CreateView):
    model = BlogPost
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']

class PostUpdateView(UpdateView):
    model = BlogPost
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']

class PostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:post_list')