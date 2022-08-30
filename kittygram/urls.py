from django.urls import include, path
from django.contrib import admin 

# from cats.views import cat_list

urlpatterns = [
   # path('cats/', cat_list),
   path('', include('cats.urls', namespace='cats')),
   path('admin/', admin.site.urls)
]


