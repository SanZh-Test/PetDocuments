from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'summarization/index.html')

def handle_uploaded_file(f):
    with open(f"uploads/{f.name}", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def upload_file(request):
    if request.method == 'POST':
        handle_uploaded_file(request.FILES['file_upload'])

    return render(request, 'summarization/upload_file.html')


def documents(request):
    return render(request, 'summarization/documents.html')


def about_us(request):
    return render(request, 'summarization/about_us.html')

