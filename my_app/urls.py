from django.urls import path
from .import views


urlpatterns=[
      path("",views.home,name='evoca'),
#     path("gents/",views.gents,name='gents'),
#     path("kids/",views.kids,name='kids')
      path("shirts/",views.shirts,name='shirts'),
      path('add_shirts/',views.add_shirts,name="new item")
]