from django.forms import ModelForm

from collection.models import List, Item

class ListForm(ModelForm):
    class Meta:
        model = List
        fields = ('name', 'description',)


# class AddEditItems(ModelForm):
#     class Meta:
#         model = List
#         fields = ('name', 'description',)