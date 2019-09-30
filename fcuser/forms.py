from django import forms
from .models import Fcuser
from django.contrib.auth.hashers import check_password


class LoginForm(forms.Form):
    username = forms.CharField(
        error_messages={
            'required': '아이디를 입력해주세요.'
        },
        max_length=32, label="사용자 이름")  # label 지정 안할 시, 템플릿에서는 기본으로 label 이 username 으로 대체
    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput, label="비밀번호")

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            try:
                fcuser = Fcuser.objects.get(username=username)
            except Fcuser.DoesNotExist:  # 예외처리!
                self.add_error('username', '아이디가 없습니다.')
                return
            if not check_password(password, fcuser.password):
                self.add_error('password', '비밀번호를 틀렸습니다.')  # 특정 필드에 에러를 넣어줌
            else:
                self.user_id = fcuser.id
