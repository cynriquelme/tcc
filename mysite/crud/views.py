from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.template import loader
from django.http import HttpResponse

from .models import City


def list_cities(request):
    cities = City.objects.all()
    template = loader.get_template('crud/cities.html')
    return HttpResponse(template.render({'cities': cities}, request))

def save_cities(request):
    #cities_save = City(description="", pub_date=timezone.now())
    city.choice_set.get(pk=request.POST['ciudad'])
    #cities_save.save()
    template = loader.get_template('crud/cities.html')
    return HttpResponse(template.render({'cities': cities_save}, request))

def save(request, city_id):
    descrip = get_object_or_404(City, pk=city_id)
    try:
        descripcion = city_set.get(pk=request.POST['ciudad'])
    except (KeyError, City.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'crud/cities.html', {
            'city': city,
            'error_message': "No se encontró la ciudad.",
        })
    else:
        descripcion.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('crud:cities', args=(city.id,)))


