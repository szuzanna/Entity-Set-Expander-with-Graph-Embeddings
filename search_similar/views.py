from django.shortcuts import render
from gensim.models import Word2Vec

def main(request):
    return render(request, 'main.html',{})


def show_results(request):
    entities = request.GET.get('entities', 'ajajaj')
    entities = entities.replace(" ", "")
    entities_list = entities.split(",")

    model = Word2Vec.load("search_similar/foodEmbedding.model")
    similarities_list = model.most_similar(entities_list)

    return render(request, 'show_results.html',{'entries': entities_list, 'similarities': similarities_list})
