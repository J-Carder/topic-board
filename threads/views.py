from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Topic
from .forms import ThreadForm, MessageForm


def index(request):
    """Home page"""
    # to display badge beside 'threads' at the top of the page
    topics = Topic.objects.all()
    context = {'topics': topics}
    return render(request, 'threads/index.html', context)


def threads(request):
    """Threads page"""
    topics = Topic.objects.order_by('-date')
    context = {'topics': topics}
    return render(request, 'threads/threads.html', context)


def thread(request, topic_id):
    """Single thread page"""

    # to display badge beside 'threads' at the top of the page
    topics = Topic.objects.order_by('-date')

    topic = Topic.objects.get(id=topic_id)
    messages = topic.message_set.order_by('date')
    context = {'topic': topic, 'topics': topics, 'messages': messages}
    return render(request, 'threads/thread.html', context)

def new_thread(request):
    """Create new thread"""
    # to display badge beside 'threads' at the top of the page
    topics = Topic.objects.order_by('-date')

    if request.method != 'POST':
        # No data, create new form
        form = ThreadForm
    else:
        # POST data submitted, process data
        form = ThreadForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('threads'))

    context = {'form': form, 'topics': topics}
    return render(request, 'threads/new_thread.html', context)

def new_message(request, topic_id):
    """Create new reply"""
    topic = Topic.objects.get(id=topic_id)
    # to display badge beside 'threads' at the top of the page
    topics = Topic.objects.order_by('-date')

    if request.method != 'POST':
        # No data, create new form
        form = MessageForm
    else:
        # POST data submitted, process data
        form = MessageForm(data=request.POST)
        if form.is_valid():
            new_message = form.save(commit=False)
            new_message.topic = topic
            new_message.save()
            return HttpResponseRedirect(reverse('thread', args=[topic_id]))

    context = {'form': form, 'topic': topic, 'topics': topics}
    return render(request, 'threads/new_message.html', context)


