from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'summarization/index.html')


def upload_file(request):
    return render(request, 'summarization/upload_file.html')


def documents(request):
    return render(request, 'summarization/documents.html')


def about_us(request):
    return render(request, 'summarization/about_us.html')

