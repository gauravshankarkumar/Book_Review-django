from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Book , Review
from django.urls import reverse


# Create your views here.

def index(request):
    data = Book.objects.all()
    return render(request, 'book_app/home.html',{'books': data})

def review(request,id):
    # return HttpResponse('Review book with id: {}'.format(id))
    data = Book.objects.get(id=id)
    reviews = Review.objects.filter(book = data)
    return render (request, 'book_app/review.html', {'book':data , 'reviews': reviews})    

def add_review(request, id):
    review_body = request.POST.get('msg')
    review_rating = request.POST.get('rating')
    review_reviewer = request.POST.get('reviewer')
    book = Book.objects.get(id=id)
    review_obj = Review(book= book , review=review_body , rating=review_rating,reviewer = review_reviewer )
    review_obj.save()
    return HttpResponseRedirect( reverse('book_app:review', args=(id)) )
