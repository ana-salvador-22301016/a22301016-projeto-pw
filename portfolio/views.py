from django.shortcuts import render
from .models import Introduction, MeByMe,TechnicalPresentation,ApplicationImages

def intro_view(request):
    intros = Introduction.objects.first()
    return render(request, 'portfolio/intro.html', {'intros': intros})

def mebyme_detail(request):
    mebymes = MeByMe.objects.all()
    return render(request, 'portfolio/aboutMe.html', {'mebymes': mebymes})



def tech_presentation(request):
    presentation = TechnicalPresentation.objects.first()
    return render(request, 'portfolio/Techpresentation.html', {'presentation': presentation})

def allApp_view(request):
    images = ApplicationImages.objects.all()
    return render(request, 'portfolio/allApp.html', {'images': images})


def video(request):
        return render(request, 'portfolio/video.html',)
