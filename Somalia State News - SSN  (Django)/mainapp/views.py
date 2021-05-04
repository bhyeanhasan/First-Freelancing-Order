from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from .models import DP
from django.core.paginator import Paginator
from django.core.mail import send_mail as sm


# Create your views here.

def dp(request):
    Post_News = DP.objects.all()
    paginator = Paginator(Post_News, 12)
    page_number = request.GET.get('page')
    print(page_number)
    page_obj = paginator.get_page(page_number)

    arti = DP.objects.filter(job__contains='1')

    if len(arti)>4:
        arti = arti[0:4];

    breaking = DP.objects.filter(breaking_news__contains='1')

    if len(breaking)>1:
        breaking = breaking[:1];

    return render(request, 'index.html', {'page_obj': page_obj, "arti": arti, "breaking": breaking})


def details(request,id):
    data = get_object_or_404(DP, id = id)
    news = DP.objects.all()

    if len(news)>6:
        news = news[0:6]
    return render(request, 'details.html', {"datas":data ,"news":news})


def articles(request):
    keyword = request.GET.get("key")
    if len(keyword) > 0:
        articles = DP.objects.filter(name__contains=keyword)
        if len(articles) > 0:
            return render(request, "articles.html", {"articles": articles})
        else:
            ob = DP()
            ob.name = 'not found'
            ob.img = 'asa.jpg'
            ob.res = 00
            articles = [ob]
            return render(request, "articles.html", {"articles": articles})
    else:
        ob = DP()
        ob.name = 'No Product Found'
        ob.img = 'asa.jpeg'
        ob.res = 000
        articles = [ob]
        return render(request, "articles.html", {"articles": articles})


def job(request):
    articles = DP.objects.filter(job__contains='1')
    return render(request, "articles.html", {"articles": articles})


def breaking(request):
    articles = DP.objects.filter(breaking_news__contains='1')
    return render(request, "articles.html", {"articles": articles})


def frypan(request):
    articles = DP.objects.filter(tag__contains='frypan')
    return render(request, "articles.html", {"articles": articles})


def editorial(request):
    articles = DP.objects.filter(editorial__contains='1')
    return render(request, "articles.html", {"articles": articles})


def rice(request):
    articles = DP.objects.filter(tag__contains='rice')
    return render(request, "articles.html", {"articles": articles})


def pressure(request):
    articles = DP.objects.filter(tag__contains='pressure')
    return render(request, "articles.html", {"articles": articles})


def blender(request):
    articles = DP.objects.filter(tag__contains='blender')
    return render(request, "articles.html", {"articles": articles})


def glass(request):
    articles = DP.objects.filter(tag__contains='glass')
    return render(request, "articles.html", {"articles": articles})


def plastic(request):
    articles = DP.objects.filter(tag__contains='plastic')
    return render(request, "articles.html", {"articles": articles})


def alu(request):
    articles = DP.objects.filter(tag__contains='alu')
    return render(request, "articles.html", {"articles": articles})


def other(request):
    articles = DP.objects.filter(tag__contains='other')
    return render(request, "articles.html", {"articles": articles})

def about_us(request):
    news = DP.objects.all()
    if len(news) > 4:
        news = news[0:4]
    return  render(request,"abut_us.html",{"news":news})

def contact_us(request):
    news = DP.objects.all()
    if len(news) > 4:
        news = news[0:4]
    return  render(request,"contact.html",{"news":news})

def send_mail(request):
    res = sm(
        subject = 'Subject here',
        message = 'Here is the message.',
        from_email = 'mail@gmail.com',
        recipient_list = ['somaliastatenews@gmail.com'],
        fail_silently=False,
    )

    return HttpResponse(f"Email sent to {res} members")