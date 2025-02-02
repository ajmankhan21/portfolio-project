from django.shortcuts import render
from django.db.models import Q
from .models import Project, Skill
from blog.models import Post
from services.models import Service

def home(request):
    """Homepage view with featured content"""
    context = {
        'featured_projects': Project.objects.filter(featured=True)[:4],
        'skills': Skill.objects.filter(show=True),
        'recent_posts': Post.objects.filter(published=True).order_by('-created_at')[:3],
        'services': Service.objects.filter(available=True)[:3]
    }
    return render(request, 'core/home.html', context)

def search(request):
    """Global search functionality"""
    query = request.GET.get('q', '')
    
    results = {
        'projects': Project.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(tech_stack__icontains=query)
        ),
        'posts': Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(excerpt__icontains=query)
        ).filter(published=True),
        'products': Product.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        ).filter(available=True),
        'services': Service.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        ).filter(available=True),
    }
    
    return render(request, 'core/search_results.html', {
        'query': query,
        'results': results
    })

def project_detail(request, slug):
    """Individual project detail view"""
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'core/project_detail.html', {'project': project})

def skills(request):
    """Full skills listing page"""
    categories = Skill.objects.values_list('category', flat=True).distinct()
    return render(request, 'core/skills.html', {
        'categories': categories,
        'skills': Skill.objects.filter(show=True)
    })