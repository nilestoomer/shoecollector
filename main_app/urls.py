from django.urls import path
from .views import Home, ShoeList, ShoeDetail, WearListCreate, WearDetail

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('shoes/', ShoeList.as_view(), name='shoe-list'),
    path('shoes/<int:id>/', ShoeDetail.as_view(), name='shoe-detail'),
    path('shoes/<int:shoe_id>/wears/', WearListCreate.as_view(), name='wear-list-create'),
	path('shoes/<int:shoe_id>/wears/<int:id>/', WearDetail.as_view(), name='wear-detail'),
]