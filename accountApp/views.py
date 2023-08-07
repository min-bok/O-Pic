from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountUpdateForm
from accountapp.models import Hello
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

has_ownership = [account_ownership_required, login_required]

@login_required # 로그인 여부를 확인하고 로그인 페이지로 리다이렉트하는 데코레이터, 클래스 내부의 메서드 함수에는 사용할 수 없음
def hello_world(request):
    if request.method == "POST":
        temp = request.POST.get("hello_input")
        # DB에 정보 저장
        new_hello = Hello()
        new_hello.text = temp
        new_hello.save()
        # DB에 저장된 정보에 접근
        list = Hello.objects.all() # Hello의 모든 데이터를 긁어옴
        
        return HttpResponseRedirect(reverse('accountapp:hello')) # account/hello로 리다이렉트
    else:
        list = Hello.objects.all()
        return render(request, "accountapp/hello.html", context={"list": list}) 



# 회원가입
class AccountCreateView(CreateView):
    model = User 
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/create.html'

# 마이페이지
class AccountDetailView(DetailView):
    model = User
    context_object_name ='target_user'
    template_name="accountapp/detail.html"

# 비밀번호 변경
@method_decorator(has_ownership, "get") # 데코레이터를 CBV에서도 사용할 수 있도록 변환해주는 데코레이터
@method_decorator(has_ownership, "post")
class AccountUpdateView(UpdateView):
    model = User 
    form_class = AccountUpdateForm
    context_object_name ='target_user'
    success_url = reverse_lazy('accountapp:hello')
    template_name = 'accountapp/update.html'

# 회원탈퇴
@method_decorator(has_ownership, "get")
@method_decorator(has_ownership, "post")
class AccountDeleteView(DeleteView):
    model = User
    context_object_name ='target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = "accountapp/delete.html"