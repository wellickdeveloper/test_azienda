from django.shortcuts import render
from .models import blogpost

from django.core.paginator import Paginator
# Create your views here.





def blog_page(request):
    articoli_database = blogpost.objects.all()
    post_totali = articoli_database.order_by('-data')
    paginator = Paginator(post_totali, 6)
    page = request.GET.get('page')
    post_totali = paginator.get_page(page)
    articoli_database = articoli_database.order_by('-data')[:4]
    context = {'articoli': articoli_database, 'post_assoluti':post_totali}
    return render(request, 'blog.html', context)







def articoli_blog(request, slug):
    oggetto = blogpost.objects.filter(slug=slug)
    articoli_database = blogpost.objects.all()
    articoli_database = articoli_database.order_by('-data')[:4]
    context = {'articoli': articoli_database, 'articolo_singolo':oggetto}
    return render(request, 'articoli.html', context)