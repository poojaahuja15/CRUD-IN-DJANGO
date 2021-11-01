from django.shortcuts import render, HttpResponseRedirect
from .forms import vehicleForm
from .models import vehicle
from django.views.generic.base import TemplateView, RedirectView
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView

def VehicleList(request):
    veh = vehicle.objects.all()
    return render(request, 'vehiclelist.html', {'v':veh})

class VehicleCreateView(SuccessMessageMixin, CreateView):
    model = vehicle
    template_name = 'add.html'
    fields = ('vehicletype', 'modelname', 'vehiclecolor', 'enginetype', )
    success_url = reverse_lazy('vehiclelist')
    success_message = "Product successfully created!"


class VehicleUpdate(SuccessMessageMixin, UpdateView):
    model = vehicle
    template_name = 'update.html'
    fields = ('vehicletype', 'modelname', 'vehiclecolor', 'enginetype', )

    def get_success_url(self):
        return reverse_lazy('vehiclelist')

class VehicleDeleteView(DeleteView):
    model = vehicle
    template_name = 'delete.html'
    success_url = reverse_lazy('vehiclelist')

