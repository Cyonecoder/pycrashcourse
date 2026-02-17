from django.shortcuts import render

from .models import Topic


# Create your views here.
def index(request):
    """The home page for Learning Log"""
    return render(request, "learning_logs/index.html")


def topics(request):
    """show all topics"""

    topics = Topic.objects.order_by("date_add")
    context = {"topics": topics}
    return render(request, "learning_logs/topics.html", context)


def topic(request, topic_id):
    """show a single topic and all its entries"""
    topic = Topic.objects.get(topic_id)
    entries = topic.entry_set.order_by("-date_add")
    context = {"topic": topic, "entries": entries}
    return render(request, "learning_logs/topic.html", context)
