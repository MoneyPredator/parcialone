from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Flight
from django.views import View
from django import forms

# Create your views here.
class Index(TemplateView):
    template_name = 'flights/index.html'

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['name', 'type', 'price']

class CreateFlight(View):
    def get(self, request):
        form = FlightForm()
        viewData = {}
        viewData["title"] = "Create product"
        viewData["form"] = form
        return render(request, self.template_name, viewData)
    
    def post(self, request):
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            viewData = {}
            viewData["title"] = "Create product"
            viewData["form"] = form
            return render(request, self.template_name, viewData)