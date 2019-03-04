from django.urls import path
from . import views


app_name = "accounts"

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # path('signup/', views.article_list, name='list'),
    # path('<slug:slug>/', views.article_detail, name='detail'),
]
