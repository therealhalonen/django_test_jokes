from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView #imported necessary Views
from . import models

class CrudListView(ListView):
    model = models.Crud

class CrudDetailView(DetailView):
    model = models.Crud
        
class CrudCreateView(CreateView):
    model = models.Crud
    fields = "__all__"
    success_url = "/"
         
class CrudUpdateView(UpdateView):
    model = models.Crud
    fields = ['name','joke'] #only edit name and the joke
    success_url = "/"  
      
class CrudUpdateYearView(UpdateView):
    model = models.Crud
    fields = ['origin'] #enable editing origin year in detailed view 

class CrudDeleteView(DeleteView):
    model = models.Crud
    success_url = "/" 
    
