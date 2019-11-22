from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

from django.http import HttpResponseRedirect

coof_like = 10000 #для тебя степ количество прибавляемых лайков при нажатии если поставиш минус лайки отниматься будут

def main(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'FreeNet/_post.html', {'posts': posts})


def addlike(request, post_id):
    post_like = get_object_or_404(Post, id=post_id)  # возвращает id статьи или 404.
    post_like.like += coof_like # Прибавляет единицу 
    post_like.save() # сохраняет
    return HttpResponseRedirect('/') # делает редирект на ту же страницу