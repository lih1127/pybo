from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Question
from django.db.models import Q, Count
import logging
logger = logging.getLogger(__name__) #__name__은 실행되는 파이썬 모듈명 'pybo'가 들어가게 됨.

def index(request):
    logger.info("INFO 레벨로 출력")
    '''
     pybo 목록출력
    '''
    #입력 파라미터
    page=request.GET.get('page','1')
    kw = request.GET.get('kw','')
    so = request.GET.get('so', 'recent')  # 정렬기준

    # 정렬
    if so == 'recommend':
        question_list = Question.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        question_list = Question.objects.annotate(num_answer=Count('answer')).order_by('-num_answer', '-create_date')
    else:  # recent
        question_list = Question.objects.order_by('-create_date')

    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |
            Q(content__icontains=kw) |
            Q(author__username__icontains=kw) |
            Q(answer__author__username__icontains=kw)
        ).distinct()

    #페이징처리
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)

    context= {'question_list': page_obj, 'page': page, 'kw':kw, 'so':so}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    question=get_object_or_404(Question, pk=question_id)
    context={'question':question}
    return render(request, 'pybo/question_detail.html', context)