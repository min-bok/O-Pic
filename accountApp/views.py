from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from accountapp.models import Hello
from django.views.generic import CreateView, DetailView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def hello_world(req):
    if req.method == "POST":
        temp = req.POST.get("hello_input")

        # DB에 정보 저장
        new_hello = Hello()
        new_hello.text = temp
        new_hello.save()

        # DB에 저장된 정보에 접근
        list = Hello.objects.all() # Hello의 모든 데이터를 긁어옴

        return HttpResponseRedirect(reverse('accountapp:hello')) # account/hello로 리다이렉트
    else:
        list = Hello.objects.all()
        return render(req, "accountapp/hello.html", context={"list": list}) 

# 계정 생성
class AccountCreateView(CreateView):
    model = User 
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello')
    template_name = 'accountapp/create.html'
