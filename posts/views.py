# Django
from django.shortcuts import render

# utilities
from datetime import datetime

posts = [
    {
        'title': 'Boreal Aurora',
        'user': {
            'name': 'Alexis Mora',
            'picture': 'https://picsum.photos/60/60'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/id/1022/536/354'
    },
    {
        'title': 'Y E E T',
        'user': {
            'name': 'Luis Lopez',
            'picture': 'https://picsum.photos/60/60'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/id/818/600/600'
    },
    {
        'title': 'Nueva Mascota!',
        'user': {
            'name': 'Jordi Roig',
            'picture': 'https://picsum.photos/60/60'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/id/433/600/600'
    },
    {
        'title': 'New Profile Pic!',
        'user': {
            'name': 'David Gavilanes',
            'picture': 'https://picsum.photos/60/60'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://i1.sndcdn.com/artworks-000516282726-jpi2xq-t500x500.jpg'
    },
]


# Create your views here.
def list_posts(request):
    """List existing posts."""
    return render(request, 'posts/feed.html', {'posts': posts})
