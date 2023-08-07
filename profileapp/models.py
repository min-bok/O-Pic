from django.contrib.auth.models import User
from django.db import models

# Create your views here.
class Profile(models.Model):
    # on_delete=models.CASCADE: user가 탈퇴하면 프로필도 사라지도록 설정
    # related_name='profile': request.user.profile처럼 바로 접근가능하도록 설정
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # upload_to='' : 이미지 저장경로 지정(media/profile/)
    image = models.ImageField(upload_to='profile/', null=True)
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)