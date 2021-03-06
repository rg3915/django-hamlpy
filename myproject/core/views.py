from django.shortcuts import render


def index(request):
    context = [
        {
            'id': 1,
            'name': 'Regis',
            'email': 'regis@email.com'
        },
        {
            'id': 2,
            'name': 'Abel',
            'email': 'abel@hotmail.com'
        },
        {
            'id': 3,
            'name': 'Fernanda',
            'email': 'fernanda@gmail.com'
        },
    ]
    return render(request, 'index.haml', {'names': context})
