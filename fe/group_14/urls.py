from django.contrib import admin
from django.urls import path
from django.urls import path, include
from .views.home import homepage, login_temp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include("customAuth.urls")),
    path('', homepage),
    path('cinema-manager/', include("cinemaManager.urls"), name="cinema_manager"),
    path('customer/', include("customer.urls")),
    path('accounts/profile/', login_temp)
]