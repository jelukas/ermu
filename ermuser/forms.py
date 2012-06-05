from django.forms import ModelForm
from models import Erm


class ErmForm(ModelForm):
    class Meta:
        model = Erm
