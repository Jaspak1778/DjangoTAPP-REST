from django import forms
from .models import Events

class AddForm(forms.ModelForm):
     class Meta:
          model = Events
          fields = '__all__'

"""
class AddForm(forms.Form):
    eventname = forms.CharField(label="Tapahtuman nimi", max_length=100) 
    startdate = forms.DateField(label="Aloituspvm", widget=forms.DateInput)       
    starttime = forms.TimeField(label="Aloitusaika", widget=forms.TimeInput)    
    enddate = forms.DateField(label="Lopetuspvm", widget=forms.DateInput)
    endtime = forms.TimeField(label="Loppuaika", widget=forms.TimeInput)
    notes = forms.CharField(label="Memo", max_length=100)

"""