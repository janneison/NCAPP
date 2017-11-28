# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse

# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render

from django.db import models

from django.contrib.auth.models import User
from django.views.generic import UpdateView

from .forms import UserProfileForm

# Create your views here.
@login_required
def index_view(request):
    return render(request, 'usuario/index.html')

def login_view(request):
    # Si el usuario esta ya logueado, lo redireccionamos a index_view
    if request.user.is_authenticated():
        return redirect(reverse('seguridad.index'))

    mensaje = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(reverse('seguridad.index'))
            else:
                mensaje = 'Cuenta inactiva'
        mensaje = 'Nombre de usuario o clave no valido'
    return render(request, 'usuario/login.html', {'mensaje': mensaje})


def logout_view(request):
	logout(request)
	messages.success(request, 'Te has desconectado con exito')
	return redirect(reverse('seguridad.login')) 

@login_required
def profile_view(request):
    return render(request, 'usuario/base_usuario.html')

class UserProfileUpdateView(UpdateView):
    model = User
    template_name = 'usuario/editar_email.html'
    
    def get_initial(self):
        initial = super(UserProfileUpdateView, self).get_initial()
        try:
            current_group = self.object.groups.get()
        except:
            # exception can occur if the edited user has no groups
            # or has more than one group
            pass
        else:
            initial['group'] = current_group.pk
        return initial
    
    def get_form_class(self):
        return UserProfileForm
    
    def form_valid(self, form):
        self.object.groups.clear()
        self.object.groups.add(form.cleaned_data['group'])
        return super(UserProfileUpdateView, self).form_valid(form)

