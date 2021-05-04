from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from django.core.paginator import Paginator
from .models import Post
from django.core.mail import send_mail as sm


def home(request):
    post = Post.objects.all()
    return render(request, "index.html", {"post": post})

def about_us(request):
    return render(request, "abut_us.html")


def service(request):
    return render(request, "service.html")


def contact_us(request):
    return render(request, "contact.html")


def send_mail(request):
    res = sm(
        subject=request.GET.get("firstname") + " " + request.GET.get("lastname"),
        message=request.GET.get("phone") + " " + request.GET.get("company") + " " + request.GET.get("subject"),
        from_email=request.GET.get("mail"),
        recipient_list=['bhyean@gmail.com'],
        fail_silently=False,
    )
    return HttpResponse(f"Email sent to {res} members")
