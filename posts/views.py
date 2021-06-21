from django.shortcuts import render, redirect

# Create your views here.
from django.template import RequestContext
from django.views.generic import *
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.edit import BaseCreateView, FormMixin
from django.views.generic.list import BaseListView

from posts.models import Post
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .forms import PostForm

from django import forms
from django.http import HttpResponseForbidden
from django.urls import reverse
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin


def mainView(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts')
    else:
        form = PostForm
        post = Post.objects.all()
        context = {
            'posts': post,
            'form': form
        }
        return render(request, 'posts/index.html', context)

# class PostFormClass(forms.Form):
#     message = forms.CharField()
#
#
# class MainView(FormMixin, DetailView):
#     model = Post
#     form_class = PostForm
#
#     def get_success_url(self):
#         return reverse('posts', kwargs={'pk': self.object.pk})
#
#     def post(self, request, *args, **kwargs):
#         if not request.user.is_authenticated:
#             return HttpResponseForbidden()
#         form = self.get_form()
#         if form.is_valid():
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)
#
#     def form_valid(self, form):
#         # Here, we would record the user's interest using the message
#         # passed in form.cleaned_data['message']
#         return super().form_valid(form)

# class PostView(ListView):
#     model = Post
#     template_name = 'posts/index.html'
#     context_object_name = 'posts'
#     fields = '__all__'
#
#
# class CreatePost(CreateView):
#     model = Post
#     template_name = 'posts/index.html'
#     fields = '__all__'


# def post_view(request):
#     post_details = Post.objects.all()
#     form = PostForm
#     context = {
#         'form': form,
#         'posts': post_details
#     }
#     return render(request, 'posts/index.html', context)

#
# class FormAndListView(BaseCreateView, BaseListView, TemplateResponseMixin):
#     model = Post
#     fields = '__all__'
#     template_name = 'posts/index.html'
#     def get(self, request, *args, **kwargs):
#         formView = BaseCreateView.get(self,request, *args, **kwargs)
#         listView = BaseListView.get(self, request, *args, **kwargs)
#         formData = formView.context_data['form']
#         listData = listView.context_data['object_list']
#         return redirect ('posts/index.html', {'form': formData, 'all_PDF': listData})


# class PageView(FormMixin, DetailView):
#     template_name = 'posts/index.html'
#     form_class = PostForm
#     model = Post
#
#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         form = self.get_form()
#         if form.is_valid():
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)
#
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)
