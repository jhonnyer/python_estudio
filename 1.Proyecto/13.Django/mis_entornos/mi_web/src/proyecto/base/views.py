from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Tarea

#from django.http import HttpResponse
#def lista_pendientes(pedido):
#    return HttpResponse('Lista de pendientes')

class Logueo(LoginView):
    template_name = "base/login.html"
    field='__all__'
    redirect_authenticated_user=True

    def get_success_url(self):
        return reverse_lazy('tareas')

class PaginaRegistro(FormView):
    template_name="base/registro.html"
    form_class=UserCreationForm
    redirect_authenticated_user=True
    success_url = reverse_lazy('tareas')

    def form_valid(self,form):
        usuario=form.save()  #Lo que haya en el formulario lo guarda en una variable llamada usuario
        if usuario is not None: #Si se registro un usuario, que se realice de una vez el logueo del usuario
            login(self.request,usuario)
        return super(PaginaRegistro,self).form_valid(form) #Retorna lo que hay en la instancia superior

    #Redefinir método get para que el usuario una vez registrado no se pueda volver a registrar, sino que lo lleve a la página inicia de 'tareas' en este caso.
    def get(self,*args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tareas')
        return super(PaginaRegistro,self).get(*args,**kwargs)  #Si no esta autenticado el usuario permite registrarse

#ListaPendientes hereda de ListView metodos para renderizar la vista
class ListaPendientes(LoginRequiredMixin, ListView):
    model = Tarea
    template_name = 'tarea_list.html'  # Reemplaza 'tarea_list.html' con la plantilla que deseas usar para mostrar los datos
    context_object_name = 'tareas'  # Nombre del objeto de contexto en la plantilla (opcional) => hace referencia a la tabla o modelo (alias)
    queryset = Tarea.objects.all()  # Define el conjunto de consultas que deseas mostrar

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['tareas']=context['tareas'].filter(usuario=self.request.user)
        context['count'] = context['tareas'].filter(completo=False).count()

        valor_buscado=self.request.GET.get('area-buscar') or ''
        if valor_buscado:
            context['tareas']=context['tareas'].filter(titulo__icontains=valor_buscado)
        context['valor_buscado']=valor_buscado
        return context

class DetalleTarea(LoginRequiredMixin, DetailView):
    model = Tarea
    template_name = 'base/tarea_detail.html'
    context_object_name = 'tarea'  # Nombre del objeto en la plantilla


class CrearTarea(LoginRequiredMixin, CreateView):
    model = Tarea
    template_name = 'base/tarea_form.html'
    #fields='__all__'  #Incorpora todos los campos del modelo
    fields=['titulo','descripcion','completo']
    success_url = reverse_lazy('tareas')

    def form_valid(self,form):
        form.instance.usuario=self.request.user
        return super(CrearTarea, self).form_valid(form)

class EditarTarea(LoginRequiredMixin, UpdateView):
    model = Tarea
    #fields = '__all__'  # Incorpora todos los campos del modelo
    fields = ['titulo', 'descripcion', 'completo']
    success_url = reverse_lazy('tareas')

class EliminarTarea(LoginRequiredMixin, DeleteView):
    model = Tarea
    context_object_name = 'tarea'  # Nombre del objeto en la plantilla
    success_url = reverse_lazy('tareas')