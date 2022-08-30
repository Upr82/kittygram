from django.urls import include, path
# from .views import cat_list, cat_detail
# from .views import APICat, APICatDetail
# from .views import CatList, CatDetail
from .views import CatViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('cats', CatViewSet)
app_name = 'cats'

urlpatterns = [
    # path('cats/', cat_list, name='cats'),
    # path('cats/<int:pk>/', cat_detail, name='cat_detail'),
    # path('cats/', APICat.as_view()),
    # path('cats/<int:pk>/', APICatDetail.as_view()),
    # path('cats/', CatList.as_view()),
    # path('cats/<int:pk>/', CatDetail.as_view()),
    path('', include(router.urls)),    
]