from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.utils import timezone
from blog.models import Post
from .forms import BlogPostForm


def post_list(request):
    """
    Create a view that will return a
    list of Posts that were published prior to'now'
    and render them to the 'blogposts.html' template
    """
    posts = Post.objects.filter(published_date__lte=timezone.now()
        ).order_by('-published_date')

    postsOrdered = Post.objects.filter(published_date__lte=timezone.now()
        ).order_by('-views')

    top5 = []
    for post in postsOrdered:
        top5.append(post)
        

    return render(request, "blogposts.html", {'posts': posts, 'top5': top5})

def post_detail(request, id):
    """
    Create a view that return a single
    Post object based on the post ID and
    and render it to the 'postdetail.html'
    template. Or return a 404 error if the
    post is not found
    """
    post  = get_object_or_404(Post, pk=id)
    post.views += 1 # clock up the number of post views
    post.save()
    posts = Post.objects.filter(published_date__lte=timezone.now()
        ).order_by('-views')
    return render(request, "postdetail.html",{'post': post, 'posts': posts})

def new_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(post_detail, post.pk)
    else:
        form = BlogPostForm()
    return render(request, 'blogpostform.html', {'form': form})

def edit_post(request, id):
   post = get_object_or_404(Post, pk=id)
   if request.method == "POST":
       form = BlogPostForm(request.POST, request.FILES, instance=post)
       if form.is_valid():
           post = form.save(commit=False)
           post.author = request.user
           post.published_date = timezone.now()
           post.save()
           return redirect(post_detail, post.pk)
   else:
       form = BlogPostForm(instance=post)
   return render(request, 'blogpostform.html', {'form': form})