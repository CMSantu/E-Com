from django.urls import path
from .views import success,category_list,category_products,about_us,product_detail,clear_cart, cart, add_to_cart, logout,signup,home,checkout,update_cart,remove_from_cart
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    path('cart/', cart, name='cart'),
    path('categories/',category_list, name='category_list'),
    path('category/<int:category_id>/',category_products, name='category_products'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('logout/', logout, name='logout'),
    path('signup/', signup, name='signup'),
    path('success/',success,name='success'),
    path('checkout/', checkout, name='checkout'),
    path('clear_cart/',clear_cart,name='Clearcart'),
    path('Update Cart/<int:pk>',update_cart,name='update_cart'),
    path('Remove/<int:pk>',remove_from_cart,name='remove_from_cart'),
    path('about_us/',about_us,name='about_us'),
    path('login/', auth_views.LoginView.as_view(template_name='shop/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
