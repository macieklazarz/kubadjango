from django.http import HttpResponse
from django.shortcuts import render
from realizacje.models import Realizacje
from tuzy.models import Marka
from akcesoria.models import Akcesoria
from uslugi.models import Uslugi
from django.core.mail import send_mail
from django.conf import settings

def homepage(request):
	if request.method =='POST':
		email = request.POST['email']
		message = request.POST['message']
		send_mail(email,
			message,
			# settings.EMAIL_HOST_USER,
			email,
			['tuzownia@gmail.com'],
			fail_silently=False)
		return render(request, 'message_sent.html')
	else:

		context = {}
		context['foto'] = Realizacje.objects.all()
		context['marki'] = Marka.objects.all()
		context['akcesoria'] = Akcesoria.objects.all()
		context['uslugi'] = Uslugi.objects.all()

	    # foto = Realizacje.objects.all()
	    # marki = Marka.objects.all()
	    # akcesoria = Akcesoria.objects.all()
	    # uslugi = Uslugi.objects.all()
	    # return render(request, 'index.html', {'foto':foto, 'marki':marki, 'akcesoria':akcesoria, 'uslugi':uslugi})
		return render(request, 'index.html', context )

def message_sent(request):
	return render(request, 'message_sent.html')