import datetime
from django.conf import settings
from django.shortcuts import render
from central.models import Post, EmailList
from central.forms import SigninForm, Contact_Me_Form, EmailList_Form
from django.shortcuts import render, get_object_or_404
from central.utils import get_read_time
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def landing_page(request):
    template = "index.html"
    title = "Home"
    post = Post.objects.prefetch_related("tags").all()
    context = {
    "post":post,
    "title":title,
    }
    return render(request, template, context)


def article_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    main_sec_url_tracking = post.url_tracking
    if not main_sec_url_tracking in request.session:
        post.hits += 1
        post.save()
        request.session[main_sec_url_tracking] = main_sec_url_tracking
    post_title = post.title.title()
    content = post.content
    meta_description = post.meta_description
    post_category = post.category
    read_time = get_read_time(content)
    post_tags = post.tags.all()
    ui_tag_status = bke_tag_status = algo_tag_status = free_tag_status = prm_tag_status  = tips_tag_status = ""

    def tags_filter(tag):
        output = post_tags.filter(tag=tag)
        return output

    if tags_filter("ui_tag"):
        ui_tag_status =  tags_filter("ui_tag")
    if tags_filter("bke_tag"):
        bke_tag_status = tags_filter("bke_tag")
    if tags_filter("algo_tag"):
        algo_tag_status = tags_filter("algo_tag")
    if tags_filter("frb_tag"):
        free_tag_status = tags_filter("frb_tag")
    if tags_filter("prm_tag"):
        prm_tag_status =  tags_filter("prm_tag")
    if tags_filter("tips_tag"):
        tips_tag_status =  tags_filter("tips_tag")

    post_image_url = post.image.url
    post_read_time = post.read_time
    post_last_updated = post.last_updated
    post_category =  post.category
    post_published =  post.timestamp
    if post_category == "premium":
        if request.user.is_staff:
            return render(request,'main/detail.html', {
              'post': post, 'read_time':read_time, 
              'post_tags':post_tags, 'ui_tag_status':ui_tag_status,
              'bke_tag_status':bke_tag_status,'algo_tag_status':algo_tag_status, 
              'free_tag_status':free_tag_status, 'prm_tag_status':prm_tag_status,
              'tips_tag_status':tips_tag_status, 'post_title':post_title,
              'post_image_url':post_image_url, 'post_read_time':post_read_time,
              'post_last_updated':post_last_updated, 'post_category':post_category,
              'meta_content':meta_description, 'post_published':post_published
            })
        else:
            status = "restricted"
            return render(request,'main/detail.html', {
              'status':status,
              'post_tags':post_tags, 'ui_tag_status':ui_tag_status,
              'bke_tag_status':bke_tag_status,'algo_tag_status':algo_tag_status, 
              'free_tag_status':free_tag_status, 'prm_tag_status':prm_tag_status,
              'tips_tag_status':tips_tag_status, 'post_title':post_title,
              'post_image_url':post_image_url, 'post_read_time':post_read_time,
              'post_last_updated':post_last_updated, 'post_category':post_category,
              'meta_content':meta_description, 'post_published':post_published
            })

    else:
        return render(request,'main/detail.html', {
            'post': post, 'read_time':read_time, 
            'post_tags':post_tags, 'ui_tag_status':ui_tag_status,
            'bke_tag_status':bke_tag_status,'algo_tag_status':algo_tag_status, 
            'free_tag_status':free_tag_status, 'prm_tag_status':prm_tag_status,
            'tips_tag_status':tips_tag_status, 'post_title':post_title,
            'post_image_url':post_image_url, 'post_read_time':post_read_time,
            'post_last_updated':post_last_updated, 'post_category':post_category,
            'meta_content':meta_description, 'post_published':post_published
        })


def categories(request):
    title = "Categories"
    template = "main/category.html"
    post = Post.objects.prefetch_related("tags").all()
    context = {
        "post":post,
        "title":title
    }
    return render(request, template, context)


def terms_of_service(request):
    title = "Terms of Service"
    template = "legal/tos.html"
    context = {
        "title":title
    }
    return render(request, template, context)

def privacy_policy(request):
    title = "Privacy Policy"
    template = "legal/pp.html"
    context = {
        "title":title
    }
    return render(request, template, context)

def cookies_policy(request):
    title = "Cookies Policy"
    template = "legal/cookies.html"
    context = {
        "title":title
    }
    return render(request, template, context)

def user_interface(request):
    title = "UI"
    template = "categories/ui.html"
    context = {
        "title":title
    }
    return render(request, template, context)
    
def backend(request):
    title = "Backend"
    template = "categories/backend.html"
    context = {
        "title":title
    }
    return render(request, template, context)

def algorithm(request):
    title = "Algorithms"
    template = "categories/algorithm.html"
    context = {
        "title":title
    }
    return render(request, template, context)

def freebies(request):
    title = "Free Projects"
    template = "categories/freebie.html"
    context = {
        "title":title
    }
    return render(request, template, context)

def premium(request):
    title = "Premium Projects"
    template = "categories/premium.html"
    context = {
        "title":title
    }
    return render(request, template, context)

def tips(request):
    title = "Tips n Tricks"
    template = "categories/tips.html"
    context = {
        "title":title
    }
    return render(request, template, context)

def contact(request):
    title = "Contact"
    template = "main/contact.html"
    form = Contact_Me_Form()
    context = {
        "title":title,
        "form": form,
    }
    return render(request, template, context)

def about(request):
    title = "About"
    template = "main/about.html"
    context = {
        "title":title
    }
    return render(request, template, context)

def post_contact(request):
    if request.method == 'POST' and request.is_ajax():
        form = Contact_Me_Form(request.POST)
        if form.is_valid():
            info = "success"
            instance = form.save(commit=False)
            instance.save()
            return JsonResponse({"success":True, "info":info}, status=200)
        else:
            info = "failure"
            return JsonResponse({"success":False, "info":info}, status=400)
    return JsonResponse({"success":False}, status=400)


def post_emaillist(request):
    if request.method == 'POST' and request.is_ajax():
        form = EmailList_Form(request.POST)
        if form.is_valid():
            info = "success"
            instance = form.save(commit=False)
            email = request.POST['email']
            all_emails = EmailList.objects.values_list('email', flat=True)
            if email in all_emails:
                info = "Already exists"
                return JsonResponse({"success":False, "info":info}, status=400)
            else:
                instance.save()
            return JsonResponse({"success":True, "info":info}, status=200)
        else:
            info = "failure"
            return JsonResponse({"success":False, "info":info}, status=400)
    return JsonResponse({"success":False}, status=400)


def search(request):
    title = "Search"
    if 'query' in request.GET and request.GET['query']:
        myquery = request.GET['query']
        myquery_caps = myquery.title()
        post = Post.objects.filter(
        Q(title__icontains=myquery)|
        Q(content__icontains=myquery)|
        Q(category__icontains=myquery)|
        Q(badges__icontains=myquery)|
        Q(read_time__icontains=myquery)|
        Q(last_updated__icontains=myquery)|
        Q(url_tracking__icontains=myquery)|
        Q(meta_description__icontains=myquery)
        ).filter(draft=False).all()
        number_of_posts = post.count()
        page = request.GET.get('page', 1)
        paginator = Paginator(post, 5)
        try:
            post_query = paginator.page(page)
        except PageNotAnInteger:
            post_query = paginator.page(1)
        except EmptyPage:
            post_query = paginator.page(paginator.num_pages)                                            
    return render(request, 'main/search_result.html', {
        'post_query': post_query,
        'query': myquery,"myquery_caps":myquery_caps,
        "title":title, "number_of_posts":number_of_posts 
    })

def csrf_byepass(request, reason=""):
    # return same page
    return redirect(request.META['HTTP_REFERER']) 


def error_500(request):
    title = "Under Maintenance"
    template = "main/under_maintenance.html"
    context = {
    "title":title
    }
    return render(request, template, context)


def brave_rewards(request):
    template = ".well-known/brave-rewards-verification.txt"
    return render(request, template, {})