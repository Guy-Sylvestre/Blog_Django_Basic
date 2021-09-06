from django.shortcuts import redirect, render
from blog.models import *
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from blog.forms import *
# Create your views here.

def dashbord(request):
    return render(request, "app_admin.html")


@login_required
def user_articles(request):
    #if not request.user.is_authenticated:
    #    return redirect('login-blog')
    has_perm = False
    if request.user.has_perm("blog.delete_article"):
        has_perm = True

    liste_articles = Article.objects.filter(user=request.user)
    context ={"liste_articles": liste_articles,
                "has_perm": has_perm
                }
    return render(request, "my_article.html", context)


class AddArticle(LoginRequiredMixin ,CreateView):
    model = Article
    form_class = ArticleForm
    template_name = "add_article.html"
    success_url = "/mes_articles/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class UpdateArticle(LoginRequiredMixin ,UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = "app_admin/article_form.html"

class DeleteArticle(LoginRequiredMixin, DeleteView):
    model = Article
    success_url = "/mes_articles/"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm("blog.delete_article"):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)