from django.urls import path
from accountapp.views import hello_world, AccountCreateView, AccountDetailView
from django.contrib.auth.views import LoginView, LogoutView

app_name = "accountapp"

urlpatterns = [
    path('hello/', hello_world, name="hello"),
    path('create/', AccountCreateView.as_view(), name="create"),
    path('login/', LoginView.as_view(template_name="accountapp/login.html"), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('detail/<int:pk>', AccountDetailView.as_view(), name="detail")
]
