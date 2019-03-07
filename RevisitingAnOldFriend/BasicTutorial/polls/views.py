# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from .models import Question
from django.shortcuts import render, get_object_or_404
# from django.http import Http404
# from django.template import loader

# V 1.0
# def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#   output = ','.join([q.question_text for q in latest_question_list])
#    return HttpResponse(output)

# V 2.0
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))


def index(request):
    latest_question_list = Question.objects.order_by('question_text')[:5]
    context = {'latest_question_list': latest_question_list, }
    return render(request, 'polls/index.html', context)

# The hard way xd
# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist, sorry.")
#     return render(request, 'polls/detail.html', {'question': question, })  # question returns __str__(self)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")
