from django.contrib import admin
from django.urls import path, include
from . import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v.home, name='home ' ),
    path('get_by_category/<int:id>/', v.get_by_category, name='get_by_category'),
    path('get_by_author/<int:id>/', v.get_by_author, name='get_by_author'),
    path('get_by_movie/<int:id>/', v.get_by_movie, name='get_by_movie'),
    path('get_by_birthday/<int:id>/', v.get_by_birthday, name='get_by_birthday'),

    path('author_list/<int:id>/', v.author_list, name='author_list'),
]