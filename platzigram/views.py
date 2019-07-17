from django.http import HttpResponse

# Utilities
from datetime import datetime
import json


def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Oh, hi! Current server time is {now}!'.format(
        now=str(now)
    ))


def sort_integers(request):
    numbers = request.GET['numbers']
    numbers = numbers.split(',')
    # a way of doing it is like:
    # numbers = list(map(int, numbers))
    # numbers_sorted = sorted(numbers)

    # but this way right below with list comprehension is much
    # cleaner and better
    numbers_sorted = sorted([int(number) for number in numbers])
    # an even cleaner way would be
    # numbers = [int(i) for i in request.GET['numbers'].split(',')]

    """ what the list comprehension basically does is
        DO: int(number)
        FOR EACH number element in numbers list
    """
    data = {
        'status': 'ok',
        'numbers': numbers_sorted,
        'message': 'Integers sorted succesfully'
    }
    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')


def say_hi(request, name, age):
    """Return a greeting."""
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello, {}!, Welcome to Platzigram'.format(name)

    return HttpResponse(message)