from django.urls import path
from app import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.StoreView.as_view(), name="store"),
    path('store/<int:pk>/', views.StaffView.as_view(), name='staff'), 
    path('calendar/<int:pk>/', views.CalendarView.as_view(), name='calendar'), 
    path('calendar/<int:pk>/<int:year>/<int:month>/<int:day>/', views.CalendarView.as_view(), name='calendar'), 
    path('booking/<int:pk>/<int:year>/<int:month>/<int:day>/<int:hour>/', views.BookingView.as_view(), name='booking'), 
    path('thanks/', views.ThanksView.as_view(), name='thanks'), 
    path('mypage/<int:year>/<int:month>/<int:day>/', views.MyPageView.as_view(), name='mypage'), 
    path('mypage/holiday/<int:year>/<int:month>/<int:day>/<int:hour>/', views.Holiday, name='holiday'), 
    path('mypage/delete/<int:year>/<int:month>/<int:day>/<int:hour>/', views.Delete, name='delete'), 

    # path('', login_required(views.StoreView.as_view()), name="store"),
    # path('', views.cusStoreView.as_view(), name="cus_store"),

    path('store_list/', views.StoreListView.as_view(), name='store_list'),
    path('staff_list/<int:store_id>/', views.StaffListView.as_view(), name='staff_list'),
    path('sss/', views.StaffTopView.as_view(), name='staff_top'),
    path('mypage/', views.MyPageView.as_view(), name='mypage'),  
]