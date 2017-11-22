from django.conf.urls import url
from . import views

urlpatterns = [
   # url(r'^registro/$', views.registro_usuario_view, name='accounts.registro'),
       url(r'^$', views.index_view, name='seguridad.index'),
    url(r'^login/$', views.login_view, name='seguridad.login'),
    url(r'^logout/$', views.logout_view, name='seguridad.logout'),
    url(r'^perfil/$', views.profile_view, name='seguridad.perfil'),

]