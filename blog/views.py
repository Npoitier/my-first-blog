from django.shortcuts import render
from django.utils import timezone
from .models import Vainqueurtour
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FormAnnee


	
def get_palmares(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
	# create a form instance and populate it with data from the request:
		form = FormAnnee(request.POST)
		form['Anneeprec'].value=form['Annee'].value
		form['CBVainqueurprec'].value=form['CBVainqueur'].value
		form['CBgrimpeurprec'].value=form['CBgrimpeur'].value
		form['CBsprinterprec'].value=form['CBsprinter'].value
        # check whether it's valid:
		if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
			
			
			form.post = Vainqueurtour.objects.get(annee=form['Annee'].value())
			return render(request, 'palmares.html', {'form': form})

    # if a GET (or any other method) we'll create a blank form
	else:
		form = FormAnnee()
		
		form.post = Vainqueurtour()
	return render(request, 'palmares.html', {'form': form})