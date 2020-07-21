from .models import Album
from django import forms

class albumsForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = [
            'title',
            'artist',         
            'released',
        ]

        widgets = {
            'birthday': forms.DateInput(format=('%m/%d%Y'),attrs=
{'class':'form-control','placeholder':'Select a date','type':'date'}),}