from django.shortcuts import render, redirect
from collection.forms import ListForm
from collection.models import List, Item
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.forms.models import inlineformset_factory

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

# add below your edit_list view
def create_list(request):
    form_class = ListForm

    # if we're coming from a submitted form, do this
    if request.method == 'POST':
        # grab the data from the submitted form and
        # apply to the form
        form = form_class(request.POST)
        if form.is_valid():
            # create an instance but don't save yet
            list = form.save(commit=False)

            # set the additional details
            list.user = request.user
            list.slug = slugify(list.name)

            # save the object
            list.save()

            # redirect to our newly created list
            return redirect('list_detail', slug=list.slug)

    # otherwise just create the form
    else:
        form = form_class()

    return render(request, 'lists/create_list.html', {
        'form': form,
        'list_list': List.objects.all()
    })

# this is the view we're updating
@login_required
def edit_list(request, slug):
    # grab the object...
    list = List.objects.get(slug=slug)

    ItemInlineFormSet = inlineformset_factory(List, Item, fields=('name',))
    form_class = ListForm

    # make sure the logged in user is the owner of the list
    if list.user != request.user:
        raise Http404

    # if we're coming to this view from a submitted form,
    # do this
    if request.method == 'POST':
        # grab the data from the submitted form and
        # apply to the form
        listform = form_class(data=request.POST, instance=list)
        itemform = ItemInlineFormSet(request.POST, request.FILES, instance=list)
        if listform.is_valid() and itemform.is_valid():
            # save the new data
            listform.save()
            itemform.save()
            return redirect('list_detail', slug=list.slug)

    # otherwise just create the form
    else:
        listform = form_class(instance=list)
        itemform = ItemInlineFormSet(instance=list)

    # and render the template
    return render(request, 'lists/edit_list.html', {
        'listform': listform,
        'itemform': itemform,
    })

# --

# def manage_books(request, author_id):
#     author = Author.objects.get(pk=author_id)
#     BookInlineFormSet = inlineformset_factory(Author, Book, fields=('title',))
#     if request.method == "POST":
#         form = BookInlineFormSet(request.POST, request.FILES, instance=author)
#         if form.is_valid():
#             form.save()
#             # Do something. Should generally end with a redirect. For example:
#             return HttpResponseRedirect(author.get_absolute_url())
#     else:
#         form = BookInlineFormSet(instance=author)
#     return render(request, 'manage_books.html', {'form': form})

# ---

def browse_by_name(request, initial=None):
    if initial:
        lists = List.objects.filter(name__istartswith=initial)
        lists = lists.order_by('name')
    else:
        lists = List.objects.all().order_by('name')

    return render(request, 'search/search.html', {
        'lists': lists,
        'initial': initial,
    })