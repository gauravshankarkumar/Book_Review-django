from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Book , Review
from .forms import UserReview
from django.urls import reverse


# Create your views here.

def index(request):
    All_book = Book.objects.all()
    return render(request, 'book_app/home.html',{'books': All_book})

def Single_Book(request, id):
    if request.method == 'POST':
        review_form = UserReview(request.POST)
        if review_form.is_valid():
            review_body = request.POST.get('review')
            review_rating = request.POST.get('rating')
            review_reviewer = request.POST.get('reviewer')
            book = Book.objects.get(id=id)
            review_obj = Review(book= book , review=review_body , rating=review_rating,reviewer = review_reviewer )
            review_obj.save()
            review_form = UserReview(request.POST)
    else:
        review_form = UserReview()
    single_book_data = Book.objects.get(id=id) 
    reviews = Review.objects.filter(book = single_book_data)
    return render (request, 'book_app/Single_Book.html', {'book':single_book_data , 'reviews': reviews, 'form':review_form})   
