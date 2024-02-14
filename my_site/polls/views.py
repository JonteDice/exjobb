from django.conf.urls import url
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework_swagger.views import get_swagger_view


from .forms import CreatePollForm
from .models import Poll

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    url("swagger/", schema_view)
]

def home(request):
    polls = Poll.objects.all()
    context = {
        'polls': polls
    }
    return render(request, 'polls/home.html', context)

def create(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreatePollForm()
    context = {
        'form': form
    }
    return render(request, 'polls/create.html', context)

def delete(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    if request.method == 'POST':
        poll.delete()
        return redirect('home')
    context = {
        'poll': poll
    }
    return render(request, "polls/delete.html", context)


def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    
    if request.method == 'POST':
        selected_option = (request.POST['poll'])
        if selected_option == 'option1':
            poll.total_1 += 1
        elif selected_option == 'option2':
            poll.total_2 += 1
        elif selected_option == 'option3':
            poll.total_3 += 1
        else:
            HttpResponse(400, 'Invalid form')

        poll.save()
        return redirect('results', poll_id)
    context = {
        "poll": poll
    }
    return render(request, 'polls/vote.html', context)

def results(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    context = {
        "poll": poll
    }
    return render(request, 'polls/results.html', context)