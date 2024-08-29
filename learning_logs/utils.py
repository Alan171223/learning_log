from django.http import Http404
from .models import Topic

def check_topic_owner(request,topic):
    """Check if the current user is the owner of the topic"""
    if topic.owner != request.user:
        raise Http404