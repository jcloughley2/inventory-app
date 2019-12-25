# from django.forms import ModelForm
# from collection.models import List, Item
# from django.forms.models import inlineformset_factory

# class ListForm(ModelForm):
#     class Meta:
#         model = List
#         fields = ('name', 'description',)

# class ItemForm(ModelForm):
#     class Meta:
#         model = Item
#         exclude = ()

# ItemFormSet = inlineformset_factory(List, Item, form=ItemForm, extra=1, can_delete=True)


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
        exclude = ()

    def __init__(self, *args, **kwargs):
        super(ListForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                Field('name'),
                Field('description'),
                Hidden('slug', 'slug-placeholder'),
                Fieldset('Add items',
                    Formset('items')), #what?
                HTML("<br>"),
                ButtonHolder(Submit('submit', 'save')), 
                )
            )

# class FamilyMemberForm(ModelForm):
#     class Meta:
#         model = FamilyMember
#         exclude = ()

# FamilyMemberFormSet = inlineformset_factory(Profile, FamilyMember, form=FamilyMemberForm, extra=1)