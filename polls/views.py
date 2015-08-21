from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import *

# Create your views here.

def index(request):
  ques_list = Question.objects.order_by('-pub_date')[:5]
  return render(request, 'polls/index.html', {'ques_list': ques_list})

def detail(request, question_id):
  try:
    question = get_object_or_404(Question, pk=question_id)
  except Question.DoesNotExist:
    raise Http404("Question does not exist")
  return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
  p = get_object_or_404(Question, pk=question_id)
  try:
    selected_choice = p.choice_set.get(pk=request.POST['choice'])
  except (KeyError, Choice.DoesNotExist):
    return render(request, 'polls/detail.html', {'question': p, 
      'error_message': "You didn't select a choice"})
  else:
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
