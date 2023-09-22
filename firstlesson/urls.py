from django.urls import path
from firstlesson.views import *

urlpatterns = [
    path("", home_view, name='home'),

]