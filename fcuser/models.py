from django.db import models


# Create your models here.
class Fcuser(models.Model):
    username = models.CharField(max_length=32,
                                verbose_name='사용자명')  # 관리자페이지에서 username 대신 사용자명으로 보임
    useremail = models.EmailField(max_length=128,
                                  verbose_name='사용자이메일')
    password = models.CharField(max_length=64,
                                verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True,  # 해당 시점의 시간이 자동으로 들어감
                                           verbose_name='등록시간')

    # admin 내(admin->Fcuser->data 리스트)에서 Fcuser 객체이름(Fcuser Object)을 대체하여 표시
    # admin.py 내에서 list_display 옵션 사용시에는 의미가 없음
    def __str__(self):
        return self.username

    class Meta:
        db_table = 'fastcampus_fcuser'
        verbose_name = '패스트캠퍼스 사용자'
        verbose_name_plural = '패스트캠퍼스 사용자'  # 복수형
