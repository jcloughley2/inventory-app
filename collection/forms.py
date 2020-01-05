from django import forms
from .models import *
from django.forms.models import inlineformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Hidden, Fieldset, Div, HTML, ButtonHolder, Submit
from .custom_layout_object import *

import re

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        exclude = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        formtag_prefix = re.sub('-[0-9]+$', '', kwargs.get('prefix', '')) 
        #print (formtag_prefix)  # Only on stdout

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.fields['name'].label = False        
        self.fields['done'].label = False
        self.helper.layout = Layout(
            Div(
                Field('done', css_class="item-done",),
                Field('name', placeholder="Add Item", css_class="item-name", autocomplete='off'),
                Field('DELETE', css_class="item-delete",),
                css_class='test formset_row-{}'.format(formtag_prefix)
            )
        )

ItemFormSet = inlineformset_factory(List, Item, form=ItemForm, fields=['done','name'], extra=1, can_delete=True)

class ListForm(forms.ModelForm):

    class Meta:
        model = List
        exclude = ['slug',]

    def __init__(self, *args, **kwargs):
        super(ListForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.fields['name'].label = False        
        self.fields['description'].label = False
        self.helper.layout = Layout(
            Div(
                Field('name', placeholder="Title", css_class="list-title", autocomplete='off'),
                Field('description', placeholder="Add Description", css_class="list-description", autocomplete='off'),
                Formset('items'),
                Field('public'),
                HTML("<br>"),
                ButtonHolder(Submit('submit', 'save')), 
            )
        )