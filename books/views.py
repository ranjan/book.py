from demoapp.books.models import Book
from django.shortcuts import render_to_response

def search(request):
  errors = []
  if 'q' in request.GET:
    q = request.GET['q']
    if not q:
      errors.append('Enter a search term.')
    elif len(q) > 20:
      errors.append('Please enter at most 20 characters.')
    else:
      books = Book.objects.filter(title__icontains=q)
      return render_to_response('search_results.html',
        {'books': books, 'query': q})
  return render_to_response('search_form.html',
    {'errors': errors})





  

