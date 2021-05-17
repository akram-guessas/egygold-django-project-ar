from django import template
from egygoldapp.models import Post,Comment

register = template.Library()
@register.inclusion_tag('egygoldapp/latest_posts.html')

def latest_posts():
    context = {
    'l_posts': Post.objects.all()[0:8]
    }
    return context

@register.inclusion_tag('egygoldapp/latest_comments.html')
def latest_comments():
    context = {
    'l_comments': Comment.objects.filter(active=True)[:8]
    }
    return context