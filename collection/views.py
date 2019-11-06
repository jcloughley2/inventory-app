from django.shortcuts import render
from collection.models import List

# the rewritten view!
def index(request):
    lists = List.objects.all().order_by('?')
    return render(request, 'index.html', {
        'lists': lists,
    })

def list_detail(request, slug):
    # grab the object...
    list = List.objects.get(slug=slug)

    # and pass to the template
    return render(request, 'lists/list_detail.html', {
        'list': list,
    })