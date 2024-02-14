from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view, renderer_classes
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer

from .forms import CreatePollForm
from .models import Poll


from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Poll
from .serializers import CreatePollSerializer

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class CreatePollAPIView(APIView):

    @swagger_auto_schema(method='get', responses={200: "good"})
    @api_view(['GET'])
    def get(self, request):
        form = CreatePollForm()
        context = {'form': form}
        return render(request, 'polls/create.html', context)
    
    @swagger_auto_schema(method='post', request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT, 
        properties={
            'question': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
            'answer_1': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
            'answer_2': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
            'answer_3': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        }
    ))
    @api_view(['POST'])
    def post(self, request, *args, **kwargs):
        serializer = CreatePollSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            redirect('home')
        redirect('home')




@api_view(['GET'])
@renderer_classes([OpenAPIRenderer, SwaggerUIRenderer])
def home(request):
    polls = Poll.objects.all()
    context = {
        'polls': polls
    }
    return render(request, 'polls/home.html', context)


@swagger_auto_schema(method='post', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT, 
    properties={
        'question': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'answer_1': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'answer_2': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'answer_3': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
    }
))
@api_view(['GET', 'POST'])
@renderer_classes([OpenAPIRenderer, SwaggerUIRenderer])
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

@api_view(['GET', 'POST'])
@renderer_classes([OpenAPIRenderer, SwaggerUIRenderer])
def delete(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    if request.method == 'POST':
        poll.delete()
        return redirect('home')
    context = {
        'poll': poll
    }
    return render(request, "polls/delete.html", context)

@api_view(['GET', 'POST'])
@renderer_classes([OpenAPIRenderer, SwaggerUIRenderer])
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

@api_view(['GET'])
@renderer_classes([OpenAPIRenderer, SwaggerUIRenderer])
def results(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    context = {
        "poll": poll
    }
    return render(request, 'polls/results.html', context)