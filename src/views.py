from django.views.generic import TemplateView
from django.shortcuts import redirect, render

# Create your views here.


class Index(TemplateView):

    template_name = "src/index.html"

    def dispatch(self, request, *args, **kwargs):

        if request.user.is_anonymous:
            print("No estas autenticado, eres un usuario anonimo")
            return redirect("/login")
        else:
            print("Estas autenticado")

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['informacion'] = "Hola..."
        #context['departamentos'] = Departamento.objects.all()
        context['primeraVez'] = 1
        context['usuario'] = self.request.user
        return context
