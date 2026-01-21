from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from .models import Project


@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def create_project(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        Project.objects.create(
            title=title,
            description=description,
            created_by=request.user
        )

        return redirect('/')

    return render(request, 'projects/create.html')


