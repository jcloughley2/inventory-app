from django.shortcuts import render
from collection.models import List

# the rewritten view!
def index(request):
    lists = List.objects.all().order_by('?')
    return render(request, 'index.html', {
        'lists': lists,
    })