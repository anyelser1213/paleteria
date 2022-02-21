from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render

from .form import loginForm

# Create your views here.


class Login(LoginView):

    template_name = "usuarios/login.html"
    #template_name = "plantillas_viejas/login copy.html"
    form_class = loginForm

#Metodo que inicia de primero
    def dispatch(self, request, *args, **kwargs):

        if request.user.is_authenticated:

            print("Estas autenticado y vas al INDEX.HTML")
            #print(request.user)
            return redirect("src:index")

        else:
            print("Entramos en login")
            #print(request.user)
            print("No estas autenticado, eres un usuario anonimo")
            return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        #print("Metodo:",self.request.method)
        #print(self.form_class())
        context['titulo'] = "Inicio de sesion"
        #context['formRegistro'] = UsuariosForm(self.request.POST or None)
        return context




        #return render(request, self.template_name, {'form': form})


class Logout(LogoutView):

    template_name = "usuarios/login.html"
    next_page = "usuarios:login"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['informacion'] = "Hola..."
        return context


