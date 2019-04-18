from django.shortcuts import render
from django.utils import timezone
from .models import Post

#def post_list(request):
#    return render(request, 'blog/post_list.html', {})

def post_list(request):
    # フィルターしなければ全部のPostが表示される
    #posts = Post.objects.all()
    # 公開したPostだけにフィルターする。さらに公開日でソートしている。
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

from .forms import PostForm

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(post_detail, pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


