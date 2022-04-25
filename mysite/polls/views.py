from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.template import loader

from .models import Question
from django.http import  HttpResponse


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):

    question = get_object_or_404(Question,pk=question_id)
    return render(request, 'polls/details.html', {'question': question})



def results(requset, question_id):
    response = "You are looking at results of question {}".format(question_id)
    return HttpResponse(response)


def votes(requset, question_id):
    response = "You are voting om question {}".format(question_id)
    return HttpResponse(response)