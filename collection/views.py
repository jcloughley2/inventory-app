from django.shortcuts import render, redirect
from collection.forms import ListForm
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

# add below your thing_detail view
def edit_list(request, slug):
    # grab the object
    list = List.objects.get(slug=slug)
    # set the form we're using
    form_class = ListForm

    # if we're coming to this view from a submitted form
    if request.method == 'POST':
        # grab the data from the submitted form and apply to
        # the form
        form = form_class(data=request.POST, instance=list)
        if form.is_valid():
            # save the new data
            form.save()
            return redirect('list_detail', slug=list.slug)

    # otherwise just create the form
    else:
        form = form_class(instance=list)

    # and render the template
    return render(request, 'lists/edit_list.html', {
        'list': list,
        'form': form,
    })

