from django.shortcuts import render, redirect
import random

def shuffle(word):
    letters = []
    for c in word:
        if c.isalpha():
            letters.append(c)

    if len(letters) <= 3:
        return word

    first_letter = letters[0]
    last_letter = letters[-1]
    middle_letters = letters[1:-1]
    random.shuffle(middle_letters)
    shuffled_letters = first_letter + ''.join(middle_letters) + last_letter

    shuffled_word = []
    i = 0
    for char in word:
        if char.isalpha():
            shuffled_word.append(shuffled_letters[i])
            i += 1
        else:
            shuffled_word.append(char)
    return ''.join(shuffled_word)

def convert_contex(content):
    i = 0
    shuffled_words = ''
    for word in content.split():
        shuffled_words += shuffle(word) + ' '
    return shuffled_words

def home(request):
    message = ''
    print("Method:", request.method)
    print("FILES:", request.FILES)
    print("POST:", request.POST)

    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        try:
            message = convert_contex(uploaded_file.read().decode('utf-8'))
        except UnicodeDecodeError:
            message = "Nie udało się odczytać pliku ( możliwe że nie jest w UTF-8)."
        request.session['message'] = message
        return redirect('home')

    message = request.session.pop('message', None)

    return render(request, 'base.html', {'message': message})
