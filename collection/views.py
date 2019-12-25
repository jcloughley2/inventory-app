from django.shortcuts import render, redirect
from collection.forms import ListForm
from collection.models import List, Item
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.forms.models import inlineformset_factory
from django.http import HttpResponse
#from django.views.generic.list import ListView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView 

class Home(ListView):
   model = List



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
        'list': list,
        'listform': listform,
        'itemform': itemform,
    })

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

from .models import *
from .forms import *
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.db import transaction

class ListCreate(CreateView):
    model = List
    template_name = 'lists/list_create.html'
    form_class = ListForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super(ListCreate, self).get_context_data(**kwargs) #what?
        
        # data.slug = slugify(list.name)
        if self.request.POST:
            data['items'] = ItemFormSet(self.request.POST) #what?
        else:
            data['items'] = ItemFormSet() #what?
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        items = context['items']
        with transaction.atomic():
            form.instance.created_by = self.request.user
            # form.instance.slug = 'testslug2'
            self.object = form.save()
            self.object.user = self.request.user
            self.object.slug = slugify(self.object.name) + "-" + str(self.object.pk)
            if items.is_valid():
                items.instance = self.object
                items.save()
        return super(ListCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('list_detail', kwargs={'slug': self.object.slug})


class ListDetail(DetailView):
    model = List
    template_name = 'lists/list_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ListDetail, self).get_context_data(**kwargs)
        return context

# def list_detail(request, slug):
#     # grab the object...
#     list = List.objects.get(slug=slug)

#     # and pass to the template
#     return render(request, 'lists/list_detail.html', {
#         'list': list,
#     })

