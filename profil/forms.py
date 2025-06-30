from django.forms import ModelForm
from . models import Barang

class FormBarang(ModelForm):
    class Meta:
        model= Barang
        fields= '__all__' 

