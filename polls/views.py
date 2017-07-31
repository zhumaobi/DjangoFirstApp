from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question
from django.template import RequestContext, loader
# Create your views here.
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:3]
	context = {
        'latest_question_list': latest_question_list,
        }
	#output = ', '.join([p.question_text for p in lastest_question_list])
	return render(request, 'polls/index.html', context)

def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question':question})

def results(request, question_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("You're voting on question %s." % question_id)