from django import forms
from .models import *
from django.forms.models import inlineformset_factory

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        exclude = ()

ItemFormSet = inlineformset_factory(List, Item, form=ItemForm, fields=['name'], extra=1, can_delete=True)

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Hidden, Fieldset, Div, HTML, ButtonHolder, Submit
from .custom_layout_object import *

class ListForm(forms.ModelForm):

    class Meta:
        model = List
        exclude = ['slug',]

    def __init__(self, *args, **kwargs):
        super(ListForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.layout = Layout(
            Div(
                Field('name'),
                Field('description'),
                Fieldset('Add items',
                    Formset('items')), #what?
                HTML("<br>"),
                ButtonHolder(Submit('submit', 'save')), 
                )
            )