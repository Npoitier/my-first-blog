from django import forms
from .models import Vainqueurtour

class FormAnnee(forms.Form):
	Annee = forms.IntegerField(min_value=1903,max_value=2015)
	CBVainqueur = forms.BooleanField(label='Vainqueur',required=False)
	CBgrimpeur = forms.BooleanField(label='Meilleur Grimpeur',required=False)
	CBsprinter = forms.BooleanField(label='Meilleur Sprinter',required=False)
	Anneeprec = forms. IntegerField(required=False,widget=forms.HiddenInput())
	CBVainqueurprec = forms.BooleanField(required=False,widget=forms.HiddenInput())
	CBgrimpeurprec = forms.BooleanField(required=False,widget=forms.HiddenInput())
	CBsprinterprec = forms.BooleanField(required=False,widget=forms.HiddenInput())
	post = Vainqueurtour()