from django.db.models import F
# from django.http import Http404 # Deprecated this in favor of `get_object_or_404`
from django.http import HttpResponse, HttpResponseRedirect
# from django.template import loader  # We deprecated this in favor of `render`
from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.urls import reverse

from .models import Question

def index(request):
    latest_questions_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_questions_list': latest_questions_list}

    # We can use Django's loader along with it's HttpResponse module to 
    # render a template with context of template variables.  
    #
    # template = loader.get_template('polls/index.html')
    # return HttpResponse(template.render(context, request))

    # Or, we can use Django's `render()` shortcut which takes a request
    # object, a template name, and an optional dictionary.
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # We can use Django's database API method `get()` and raise Http404
    # if we want to:

    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist.")

    # Or, we can use another Django shortcut. This reduces coupling 
    # between our Models and our Views.

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except:
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
