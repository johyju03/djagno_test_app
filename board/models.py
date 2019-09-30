from django.db import models


# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=128,
                             verbose_name='제목')  # 관리자페이지에서 username 대신 사용자명으로 보임
    contents = models.TextField(verbose_name='내용')
    writer = models.ForeignKey('fcuser.Fcuser', verbose_name='작성자',
                               on_delete=models.CASCADE)  # 사용자 테이블에서 사용자삭제시, 관련된 board 데이터 같이 삭제
    tags = models.ManyToManyField('tag.Tag', verbose_name='태그')
    registered_dttm = models.DateTimeField(auto_now_add=True,  # 해당 시점의 시간이 자동으로 들어감
                                           verbose_name='등록시간')

    # admin 내(admin->Fcuser->data 리스트)에서 Fcuser 객체이름(Fcuser Object)을 대체하여 표시
    # admin.py 내에서 list_display 옵션 사용시에는 의미가 없음
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'fastcampus_board'
        verbose_name = '패스트캠퍼스 게시글'
        verbose_name_plural = '패스트캠퍼스 게시글'  # 복수형
