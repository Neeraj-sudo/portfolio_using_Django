from django.shortcuts import render

# Create your views here.
from projects_app.models import Project, About, Education, Skills, Work_experience, Certification


def project_index(request):
	projects = Project.objects.all()
	context = {
		'projects':projects
	}
	return render(request, 'project_index.html',context)


def project_detail(request, pk):

    project = Project.objects.get(pk=pk)

    context = {

        'project': project

    }

    return render(request, 'project_detail.html', context)


def About_page(request):

    about_data = About.objects.all()

    context = {

        'about': about_data
    }

    return render(request, 'about.html', context)


def Skills_page(request):
    skills_data = Skills.objects.all()

    context = {

        'skills_data': skills_data
    }

    return render(request, 'skills.html', context)



def Education_page(request):
    education_data = Education.objects.all()

    context = {

        'education_data': education_data
    }

    return render(request, 'education.html', context)


def Certification_page(request):
    certi_data = Certification.objects.all()

    context = {

        'certi_data': certi_data
    }

    return render(request, 'certification.html', context)


def Work_exp_page(request):
    work_data = Work_experience.objects.all()

    context = {

        'work_data': work_data
    }

    return render(request, 'work_experience.html', context)
