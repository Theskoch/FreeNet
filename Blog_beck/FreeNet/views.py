from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, masege
from .forms import masegeForm

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

def post_datail(request, post_id):
    auth = request.user
    if request.method == "POST":
        form = masegeForm(request.POST)
        if form.is_valid():
            masege_s = form.save(commit=False)
            masege_s.hesh = "#" + str(post_id)
            masege_s.post_fazer = post_id
            masege_s.fazer = post_id
            masege_s.author = auth
            masege_s.save()
            form = masegeForm()
            post = Post.objects.filter(id__contains = post_id)
            maseges = masege.objects.filter(post_fazer__contains = post_id)
            return render(request, 'FreeNet/post_datail.html', {'post': post, 'maseges': maseges, 'form': form})
    else:
        form = masegeForm()
        post = Post.objects.filter(id__contains = post_id)
        maseges = masege.objects.filter(post_fazer__contains = post_id)
    return render(request, 'FreeNet/post_datail.html', {'post': post, 'maseges': maseges, 'form': form})

def user_info(request):
    return render(request,'FreeNet/user_info.html')

def user_logout(request):
    return render(request, 'registration/logged_out.html')