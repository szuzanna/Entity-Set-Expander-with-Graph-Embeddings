from django.shortcuts import render, redirect
from gensim.models import Word2Vec
from django.urls import reverse

def main(request, **kwargs):
    return render(request, 'main.html', kwargs)


def show_results(request):
    entities = request.GET.get('entities', '')
    entities = entities.replace(", ", ",")
    entities_list = entities.split(",")

    model = Word2Vec.load("search_similar/foodEmbedding.model")
    try:
        similarities_list = model.most_similar(entities_list)
    except:
        #return render(None,'main.html', {'warning': "Make sure all node names are in database!"})
        #return redirect(reverse('main', kwargs={'warning' :'Make sure all node names are in database!'}))
        return redirect('main')#, kwargs={'warning':'Make sure all node names are in database!'})
        
    else:
        return render(request, 'show_results.html',{'entries': entities_list, 'similarities': similarities_list})
