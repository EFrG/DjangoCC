from django.shortcuts import render, get_object_or_404

from .models import Question, Choice

# First View
# Get question and display them

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request,'polls/index.html',context)
# Create your views here.
def detail(request, question_id):
    try:
        question = Question.objects.get(pk= question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request,'polls/results.html',{'question': question})

 # Get question and display results
def results (request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', { 'question': question })
