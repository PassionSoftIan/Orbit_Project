from allauth.account.adapter import DefaultAccountAdapter
from .models import User

class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        user = super().save_user(request, user, form, commit=False)
        nick_name = request.data.get('nick_name', '')  # 요청 데이터에서 nick_name 값 가져오기
        
        if User.objects.filter(nick_name=nick_name).exists():
            raise ValueError('중복된 닉네임입니다.')

        user.nick_name = nick_name
        if commit:
            user.save()
        return user
