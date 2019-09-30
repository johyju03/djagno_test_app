from django.shortcuts import render, redirect
from fcuser.models import Fcuser
from django.http import Http404
from .models import Board
from .forms import BoardForm
from tag.models import Tag
from django.core.paginator import Paginator


# Create your views here.
def board_detail(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404('게시글을 찾을 수 없습니다.')
    return render(request, 'board_detail.html', {'board': board})


def board_write(request):
    # 사용자 있는지부터 확인
    if not request.session.get('user'):
        return redirect('/fcuser/login')

    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            fcuser = Fcuser.objects.get(pk=user_id)

            tags = form.cleaned_data['tags'].split(',')
            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = fcuser
            board.save()
            for tag in tags:
                if not tag:
                    continue
                _tag, _ = Tag.objects.get_or_create(
                    name=tag)  # 일치하는 모델이 있으면 가져오고, 없으면 생성 (created = True or False 로 넘어옴)
                # board 의 id가 생성된 이후에 추가 가능하다.
                board.tags.add(_tag)

            return redirect('/board/list')
    else:
        form = BoardForm()
    return render(request, 'board_write.html', {'form': form})


def board_list(request):
    all_boards = Board.objects.all().order_by('-id')  # - 는 역순을 의미 (최신순)
    page = int(request.GET.get('p', 1))
    paginator = Paginator(all_boards, 3)

    boards = paginator.get_page(page)

    return render(request, 'board_list.html', {'boards': boards})
