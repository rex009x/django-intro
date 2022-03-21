from django.shortcuts import render
from django.http import HttpResponseBadRequest
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# Create your views here.

# initialize predefined entries
results = [{'name': 'Fatima Lopez', 'email': 'f.lopez@email.com'},
           {'name': 'Gary Johnston', 'email': 'g.johnston@email.com'}]

def index(request):
  if request.POST:
    context = {
      'name': request.POST['name'],
      'email': request.POST['email'],
    }
    # check if entries are left blank
    if context['name'] == '' or context['email'] == '':
      return HttpResponseBadRequest('<h1>The name or email field is left empty.</h1>')
    
    # check for email validity
    try:
      validate_email(context['email'])
    except ValidationError:
      return HttpResponseBadRequest('<h1>Please enter a valid email.</h1>')
    
    # valid post request, proceed to append entry
    results.append({'name': request.POST['name'], 'email': request.POST['email']})
    return render(request, 'thanks.html', context)
  # redefined context with new results if any
  context = {
    'results': results
  }
  return render(request, 'index.html', context)
