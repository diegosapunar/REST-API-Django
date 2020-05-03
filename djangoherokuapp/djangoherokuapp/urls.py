"""djangoherokuapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# SOURCE: Tarea1

from django.contrib import admin
from django.urls import path

from herokuapp import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('hamburguesa', views.hamburguesa_list, name='hamburguesas'),
    path('hamburguesa/<int:pk>', views.hamburguesa_detail, name='hamburguesa'),
    path('ingrediente', views.ingrediente_list, name='ingredientes'),
    path('ingrediente/<int:pk>', views.ingrediente_detail, name='ingrediente'),
    path('hamburguesa/<int:pk1>/ingrediente/<int:pk2>', views.edit, name='edit'),




    # path('episode/<int:episode_id>/', views.episode, name='episode'),


]
