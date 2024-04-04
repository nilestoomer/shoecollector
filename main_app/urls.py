from django.urls import path
from .views import Home, ShoeList, ShoeDetail,  WearListCreate, WearDetail, SockList, SockDetail, AddSockToShoe

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('shoes/', ShoeList.as_view(), name='shoe-list'),
    path('shoes/<int:id>/', ShoeDetail.as_view(), name='shoe-detail'),
    path('shoes/<int:shoe_id>/wears/', WearListCreate.as_view(), name='wear-list-create'),
	path('shoes/<int:shoe_id>/wears/<int:id>/', WearDetail.as_view(), name='wear-detail'),
    path('socks/', SockList.as_view(), name='sock-list'),
    path('socks/<int:id>/', SockDetail.as_view(), name='sock-detail'),
    path('shoes/<int:shoe_id>/add_sock/<int:sock_id>/', AddSockToShoe.as_view(), name='add-sock-to-shoe'),
]