from django.db.models import query
from django.shortcuts import render
from .models import Article
# Create your views here.


def home(request):
    
    #Afficher tout les élément de la base de données
    list_articles = Article.objects.all()
    
    #Retourner ces informations
    context = {"liste_articles": list_articles}
    
    return render(request, 'index.html', context)


def detail(request, id_article):
    article = Article.objects.get(id=id_article)
    
    #Article en relation avec sa catégorie
    categorie = article.category
    articleEnRelation = Article.objects.filter(category=categorie)[:6]
    
    context = {
        "article": article,
        "aer": articleEnRelation
        }
    return render(request, 'detail.html', context)



def search(request):
    query=request.GET["article"]
    liste_article = Article.objects.filter(title__contains=query)
    return render(request, "search.html", {"liste_article": liste_article})