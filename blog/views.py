from django.shortcuts import render
from django.utils import timezone
from .models import Vainqueurtour
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Selec

def post_list(request):
    posts = Vainqueurtour.objects.all() #filter(published_date__lte=timezone.now()).order_by('published_date')
    return redirect('blog.views.post_detail', pk=0) #render(request, 'blog/post_list.html', {'posts': posts})
	
def post_detail(request, pk):
	try:
		post = Vainqueurtour.objects.get(annee=pk) #post = get_object_or_404(Vainqueurtour, annee=pk)
	except Vainqueurtour.DoesNotExist:
		post = Vainqueurtour()
	return render(request, 'blog/post_detail.html', {'post': post})
	
def get_name(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
	# create a form instance and populate it with data from the request:
		form = Selec(request.POST)
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
			return render(request, 'name.html', {'form': form})

    # if a GET (or any other method) we'll create a blank form
	else:
		form = Selec()
		test = 0
		form.post = Vainqueurtour()
	return render(request, 'name.html', {'form': form})