from django.conf.urls import url
from . import views

from .views import (
    EventoList,
    EventoDetail,
    EventoCreation,
    EventoUpdate,
    EventoDelete
)

urlpatterns = [

    url(r'^$', EventoList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', EventoDetail.as_view(), name='detail'),
    url(r'^nuevo$', EventoCreation.as_view(), name='new'),
    url(r'^editar/(?P<pk>\d+)$', EventoUpdate.as_view(), name='edit'),
    url(r'^borrar/(?P<pk>\d+)$', EventoDelete.as_view(), name='delete'),
]

'''
    # ex: /eventos/
    path('', views.login, name='login'),

    # ex: /eventos/
    path('eventos/', views.index, name='index'),

    # ex: /eventos/5/
    path('eventos/<int:evento_id>/', views.detail, name='detail'),

    path('eventos/new/', views.new_event, name='new_event'),

    # ex: /polls/5/results/
    #path('<int:evento_id>/results/', views.ResultsView.as_view(), name='results'),
'''