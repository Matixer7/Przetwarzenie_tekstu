from django.shortcuts import render


def home(request):
    message = None
    print("Method:", request.method)
    print("FILES:", request.FILES)
    print("POST:", request.POST)
    if request.method == 'POST' and request.FILES.get('file'):
        print("1")
        uploaded_file = request.FILES['file']
        try:
            message = uploaded_file.read().decode('utf-8')
        except UnicodeDecodeError:
            message = "Nie udało się odczytać pliku (nie jest w UTF-8)."

    return render(request, 'base.html', {'message': message})
