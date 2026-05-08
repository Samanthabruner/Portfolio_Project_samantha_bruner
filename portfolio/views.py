from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from .models import Project, Skill


def _attach_technology_lists(projects):
    for project in projects:
        project.technology_list = [item.strip() for item in project.technologies.split(',') if item.strip()]
    return projects

def home(request):
    featured_projects = _attach_technology_lists(Project.objects.all())
    skills = Skill.objects.all()[:6]
    context = {
        'featured_projects': featured_projects,
        'skills': skills,
    }
    return render(request, 'portfolio/home.html', context)

def about(request):
    skills = Skill.objects.all()
    context = {
        'skills': skills,
    }
    return render(request, 'portfolio/about.html', context)

def projects(request):
    all_projects = _attach_technology_lists(Project.objects.all())
    category = request.GET.get('category')
    
    context = {
        'projects': all_projects,
    }
    return render(request, 'portfolio/projects.html', context)

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.technology_list = [item.strip() for item in project.technologies.split(',') if item.strip()]
    related_projects = Project.objects.exclude(pk=pk)[:3]
    related_projects = _attach_technology_lists(related_projects)
    context = {
        'project': project,
        'related_projects': related_projects,
    }
    return render(request, 'portfolio/project_detail.html', context)

def skills(request):
    all_skills = Skill.objects.all()
    categories = Skill.objects.values_list('category', flat=True).distinct()
    
    context = {
        'skills': all_skills,
        'categories': categories,
    }
    return render(request, 'portfolio/skills.html', context)

def resume(request):
    return render(request, 'portfolio/resume.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Validate form
        if not all([name, email, subject, message]):
            return JsonResponse({'success': False, 'error': 'All fields are required'})
        
        # Send email
        try:
            send_mail(
                f'Portfolio Contact: {subject}',
                f'From: {name} ({email})\n\n{message}',
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL],
            )
            return JsonResponse({'success': True, 'message': 'Message sent successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    
    return render(request, 'portfolio/contact.html')
