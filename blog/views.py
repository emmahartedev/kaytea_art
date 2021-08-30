from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Blog
from .forms import BlogForm

from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


# Create your views here.
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
    }

    return render(request, 'blog/blog.html', context)


# Create your views here.
def blog_detail(request, blog_id):
    '''A view to show individual blog details'''
    blog = get_object_or_404(Blog, pk=blog_id)
    # Show 25 contacts per page.

    context = {
        'blog': blog,
    }

    return render(request, 'blog/blog_detail.html', context)


@login_required
def add_blog(request):
    """ A view to add a blog post """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('blog', args=[blog.id]))
        else:
            messages.error(request, 'Failed to add blog. Please ensure the form is valid.')
    else:
        form = BlogForm()

    template = 'blog/add_blog.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
