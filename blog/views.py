from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Blog, Reply
from .forms import BlogForm, ReplyForm

from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def all_blogs(request):
    '''A view to return all blogs'''
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 3)
    # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'blogs': blogs,
        'page_obj': page_obj,
        'on_blog_page': True,
    }

    return render(request, 'blog/blog.html', context)


def blog_detail(request, blog_id):
    '''A view to show the details of an individual blog'''
    blog = get_object_or_404(Blog, pk=blog_id)
    # Show 25 contacts per page.
    replies = blog.replies.all().order_by('-id')
    username = None

    if request.method == "POST":
        form = ReplyForm(request.POST)

        if form.is_valid():
            user = User.objects.get(username=request.user.username)
            form.instance.author = user
            reply = form.save(commit=False)
            reply.blog = blog
            reply.save()
            messages.success(request, 'Your reply was successfully saved!')
            return redirect(reverse('blog_detail', args=[blog.id]))
    else:
        form = ReplyForm()

    context = {
        'blog': blog,
        'replies': replies,
        'form': form,
        'username': username,
        'on_blog_page': True,
    }

    return render(request, 'blog/blog_detail.html', context)


@login_required
def add_blog(request):
    ''' A view to add a blog post '''
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.get(username=request.user.username)
            form.instance.author = user
            blog = form.save()
            messages.success(request, 'Successfully added blog!')
            return redirect(reverse('blog_detail', args=[blog.id]))
        else:
            messages.error(request, 'Failed to add blog. \
                Please ensure the form is valid.')
    else:
        form = BlogForm()

    template = 'blog/add_blog.html'
    context = {
        'form': form,
        'on_blog_page': True,
    }

    return render(request, template, context)


@login_required
def edit_blog(request, blog_id):
    ''' A view to edit a blog post '''
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('blog'))

    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated blog!')
            return redirect(reverse('blog_detail', args=[blog.id]))
        else:
            messages.error(request, 'Failed to update blog. \
                 Please ensure the form is valid.')
    else:
        form = BlogForm(instance=blog)
        messages.info(request, f'You are editing {blog.title}')

    template = 'blog/edit_blog.html'
    context = {
        'form': form,
        'blog': blog,
        'on_blog_page': True,
    }

    return render(request, template, context)


@login_required
def delete_blog(request, blog_id):
    ''' Delete a blog post '''
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('blog'))
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()
    messages.success(request, 'blog deleted!')
    return redirect(reverse('blog'))


@login_required
def delete_reply(request, reply_id):
    ''' Delete a comment from a blog details page '''
    reply = get_object_or_404(Reply, pk=reply_id)
    blog_id = reply.blog.id
    blog = get_object_or_404(Blog, pk=blog_id)
    user = User.objects.get(username=request.user.username)
    author = reply.author

    if reply.author != request.user:
        print('not equal')
    else:
        print('equal')

    if reply.author != request.user and not request.user.is_superuser:
        messages.error(request, 'Sorry, you do not have permssion \
            to delete a comment.')
        print(user, author)
        return redirect(reverse('blog_detail', args=[blog.id]))

    reply = get_object_or_404(Reply, pk=reply_id)
    reply.delete()
    messages.success(request, 'Comment successfully deleted.')

    return redirect(reverse('blog_detail', args=[blog.id]))


@login_required
def edit_reply(request, reply_id):
    ''' A view to edit a blog post comment '''
    reply = get_object_or_404(Reply, pk=reply_id)
    blog_id = reply.blog.id
    blog = get_object_or_404(Blog, pk=blog_id)
    # user = User.objects.get(username=request.user.username)
    replies = blog.replies.all().order_by('-id')

    if reply.author != request.user and not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('blog'))

    if request.method == 'POST':
        form = ReplyForm(request.POST, request.FILES, instance=reply)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated comment!')
            return redirect(reverse('blog_detail', args=[blog.id]))
        else:
            messages.error(request, 'Failed to update comment. \
                Please ensure the form is valid.')
    else:
        form = ReplyForm(instance=reply)
        messages.info(request, f'You are editing \
             your comment for {reply.blog}')

    template = 'blog/edit_reply.html'

    context = {
        'reply': reply,
        'replies': replies,
        'blog': blog,
        'form': form,
        'on_blog_page': True,
    }

    return render(request, template, context)
