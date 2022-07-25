from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


from .models import Article, Section, Status

class ArticleNavbarHelper:
    def __init__(self, context):
        self.set_section(context)
        self.set_status(context)

    def set_section(self, context):
        context["section"]= Section.objects.all()
    def set_status(self, context):
        context["status"]= Status.objects.all()

class ArticleListView(ListView):
    template_name="articles/list.html"
    model = Article

    def get_article_list_context(self, context, section, status):
        context["article_list"]= Article.objects.filter(
                section=section
            ).filter(
                status=status
            ).order_by("created_on").reverse()
        return context

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["article_list"]= Article.objects.order_by("created_on").reverse()
        return context


class ArticleCreateView(CreateView):
    template_name="articles/new.html"
    model=Article
    fields=["title", "subtitle", "body", "status", "section","_type" ]

    def form_valid(self, form):
        form.instance.author= self.request.user
        return super().form_valid(form)



class ArticleDetailView(DetailView):
    template_name= "articles/detail.html"
    model = Article
    
class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name="articles/edit.html"
    model= Article
    fields= ["title", "subtitle", "body", "status"]
    
    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name="articles/delete.html"
    model= Article
    success_url: reverse_lazy("article_list")

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user