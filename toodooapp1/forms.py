from django.forms import ModelForm
from .models import toodoo

class toodooform(ModelForm):
    class Meta:
        model = toodoo
        fields = '__all__'