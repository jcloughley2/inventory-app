from django.forms import ModelForm

from collection.models import List

class ListForm(ModelForm):
    class Meta:
        model = List
        fields = ('name', 'description',)