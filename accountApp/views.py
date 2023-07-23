from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from accountapp.forms import AccountUpdateForm
from accountapp.models import Hello
from django.views.generic import CreateView, DetailView, UpdateView
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

# 회원가입
class AccountCreateView(CreateView):
    model = User 
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello')
    template_name = 'accountapp/create.html'

# 마이페이지
class AccountDetailView(DetailView):
    model = User
    context_object_name ='target_user'
    template_name="accountapp/detail.html"

# 비밀번호 변경
class AccountUpdateView(UpdateView):
    model = User 
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:hello')
    template_name = 'accountapp/update.html'