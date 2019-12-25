from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question
from django.urls import reverse
import logging

# XY on graph
political_location = [0, 0]
center_top = 48.55
center_left = 49.8


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'politilive/detail.html', {'question': question, 'political_location': political_location,
                                                      'top_align': center_top + 4.27*political_location[1], 'left_align': center_left + 1.33*political_location[0]})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = request.POST['choice']
    except:
        # Redisplay the question voting form.
        return render(request, 'politilive/detail.html', {
            'question': question,
            'error_message': "Please choose how you feel about the statement.",
        })

    delta = question.get_change(selected_choice)
    political_location[0] += delta[0]
    political_location[1] += delta[1]
    logging.getLogger('Logger').info(
        'Question #' + str(question_id) + ' user chose ' + str(selected_choice) +
        ' political location moved to ' + str(political_location))

    next_question = get_object_or_404(Question, pk=question_id+1)
    return render(request, 'politilive/detail.html', {'question': next_question, 'political_location': political_location,
                                                      'top_align': center_top + 4.27*political_location[1], 'left_align': center_left + 1.33*political_location[0]})


def index(request):
    return render(request, 'politilive/index.html')


def reset(request):
    question = get_object_or_404(Question, pk=1)
    logging.getLogger('Logger').info('STARTING NEW QUIZ')
    political_location[0] = 0
    political_location[1] = 0
    return render(request, 'politilive/detail.html', {'question': question, 'political_location': '[0, 0]',
                                                      'top_align': center_top + 4.27*political_location[1], 'left_align': center_left + 1.33*political_location[0]})
