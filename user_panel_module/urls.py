from django.urls import path
from .views import *

urlpatterns = [
    path('', UserPanelView.as_view(), name='user_panel'),
    path('edit-panel', EditUserPanelView.as_view(), name='edit_user_panel'),
    path('change-pass', ChangePasswordView.as_view(), name='change_password'),
    path('user-basket', UserBasket.as_view(), name='user_basket'),
    path('remove-order-detail/', remove_order_detail, name='remove_order_detail'),
    path('change-order-detail-count', change_order_detail_count, name='change_order_detail_count'),
]
