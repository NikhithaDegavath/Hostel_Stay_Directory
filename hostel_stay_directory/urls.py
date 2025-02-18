from django.urls import path
from hostel import views

urlpatterns = [
    path('', views.start, name='start'),  # Starting page
    path('home/', views.home, name='home'),  # Home page
    path('user-login/', views.user_login, name='user_login'),  # User login page
    path('admin-login/', views.admin_login, name='admin_login'),  # Admin login URL
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),  # Admin dashboard URL
    path('add-person/', views.add_person, name='add_person'),  # Add Person URL
    path('add-room/', views.add_room, name='add_room'),
    path('checkin-checkout/', views.checkin_checkout, name='checkin_checkout'),
    path('checkin/', views.checkin, name='checkin'),
    path('checkout/', views.checkout, name='checkout'),
    path('user-login/', views.user_login, name='user_login'),  # User login URL
    path('leave-application/', views.leave_application, name='leave_application'),
    path('view-info/', views.view_info, name='view_info'),
    path('visitor-info/', views.visitor_info, name='visitor_info'),
    path('fee-detail/', views.fee_detail, name='fee_detail'),
    path('user-dashboard/', views.user_dashboard, name='user_dashboard'),
    path('feedback/', views.feedback, name='feedback'),
    path('logout/', views.logout, name='logout'),
    path('view-info/', views.view_info, name='view_info'),
    path('all-persons-info/', views.all_persons_info, name='all_persons_info'),
    path('room-info/', views.room_info, name='room_info'),
    path('admin-feedback/', views.admin_feedback, name='admin_feedback'),  # Admin feedback URL
]