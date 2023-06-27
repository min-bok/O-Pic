from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from accountapp.models import Hello
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def hello_world(req):
    if req.method == "POST":
        temp = req.POST.get("hello_input")

        new_hello = Hello()
        new_hello.text = temp
        new_hello.save()

        global list
        list = Hello.objects.all() # Hello의 모든 데이터를 긁어옴

        return HttpResponseRedirect(reverse('accountapp:hello')) # account/hello로 리다이렉트
    else:
        return render(req, "accountapp/hello.html", context={"list": list}) 

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accounapp/hello.html')
    template_name = "accountapp/create.html"