from central.models import Post, TagChoices
from central.utils import get_read_time
from central.forms import EmailList_Form
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def category_limiter(category_type, limit):
    """
    where category_type is a variable that contains the queryset of a specific     
    category and limit is an integer to denote the total number of blog posts 
    to display by category
    category_type: var
    limit: int
    """
    return category_type[:limit]


def major_data(request):
    canonical_path = request.build_absolute_uri(request.path)
    email_form = EmailList_Form()
    all_post_non_draft = Post.objects.filter(draft=False).all()

    def hits_limiter(limit):
        """
        where limit is the total number of blogposts to display based on the highest
        hits
        limit: int
        
        """
        return all_post_non_draft.order_by('-hits')[:limit]

    def newest_post(limit):
        """
        where limit is the total number of blogposts to display based on the highest
        hits
        limit: int
        
        """
        return all_post_non_draft.order_by('-timestamp')[:limit]


    # top three posts on specific categories
    all_post_non_draft_t3 = category_limiter(all_post_non_draft, 3)

    # post based on highest hits
    posts_by_hits = hits_limiter(3)

    # post based on time posted
    newest_post = newest_post(1)

    # return all in context
    return {
            "all_post_non_draft" : all_post_non_draft,
            "all_post_non_draft_t3":all_post_non_draft_t3,
            "posts_by_hits":posts_by_hits,
            "canonical_path":canonical_path,
            "newest_post":newest_post
            }


def pagination_data(request):
    # number of posts to display per pagination
    NUM_POST = 10

    # pages
    def page_identifier(spec_page):
        """
        where page_identifier is a sub-function that gets and return a specific
        page. It takes in a string as an parameter.
        limit: str

        """
        page = request.GET.get(spec_page, 1)
        return page

    ui_page = page_identifier('ui_page')
    bke_page = page_identifier('bke_page')
    algo_page = page_identifier('algo_page')
    freebie_page = page_identifier('freebie_page')
    prm_page = page_identifier('prm_page')
    tips_page = page_identifier('tips_page')
    
    # pagination for ui
    ui_category = Post.objects.filter(draft=False, category= "ui").all()
    ui_category_count = len(ui_category)
    ui_category_paginator = Paginator(ui_category, NUM_POST)
    ui_category_t3 = category_limiter(ui_category, 3)
    

    # pagination for backend
    backend_category = Post.objects.filter(draft=False, category= "backend").all()
    backend_category_count = len(backend_category)
    backend_category_paginator = Paginator(backend_category, NUM_POST)
    backend_category_t3 = category_limiter(backend_category, 3)
    

    # pagination for algorithm
    algorithm_category = Post.objects.filter(draft=False, category= "algorithm").all()
    algorithm_category_count = len(algorithm_category)
    algorithm_category_paginator = Paginator(algorithm_category, NUM_POST)
    algorithm_category_t3 = category_limiter(algorithm_category, 3)
    

    # pagination for free-projects
    freeproject_category = Post.objects.filter(draft=False, category= "freebies").all()
    freeproject_category_count = len(freeproject_category)
    freeproject_category_paginator = Paginator(freeproject_category, NUM_POST)
    freeproject_category_t3 = category_limiter(freeproject_category, 3)
    

    # pagination for premium-projects
    premium_category = Post.objects.filter(draft=False, category= "premium").all()
    premium_category_count = len(premium_category)
    premium_category_paginator = Paginator(premium_category, NUM_POST)
    premium_category_t3 = category_limiter(premium_category, 3)
    

    # pagination for tips/tricks
    tips_category = Post.objects.filter(draft=False, category= "tips_n_tricks").all()
    tips_category_count = len(tips_category)
    tips_category_paginator = Paginator(tips_category, NUM_POST)
    tips_category_t3 = category_limiter(tips_category, 3)

    try:
        ui_category_post_query = ui_category_paginator.page(ui_page)
        backend_category_post_query = backend_category_paginator.page(bke_page)
        algorithm_category_post_query = algorithm_category_paginator.page(algo_page)
        tips_category_post_query = tips_category_paginator.page(tips_page)
        freeproject_category_post_query = freeproject_category_paginator.page(freebie_page)
        premium_category_post_query = premium_category_paginator.page(prm_page)

    except PageNotAnInteger:
        ui_category_post_query = ui_category_paginator.page(1)
        backend_category_post_query = backend_category_paginator.page(1)
        algorithm_category_post_query = algorithm_category_paginator.page(1)
        tips_category_post_query = tips_category_paginator.page(1)
        freeproject_category_post_query = freeproject_category_paginator.page(1)
        premium_category_post_query = premium_category_paginator.page(1)

    except EmptyPage:
        ui_category_post_query = ui_category_paginator.page(ui_category_paginator.num_pages)
        backend_category_post_query = backend_category_paginator.page(ui_category_paginator.num_pages)
        algorithm_category_post_query = algorithm_category_paginator.page(algorithm_category_paginator.num_pages)
        tips_category_post_query = tips_category_paginator.page(tips_category_paginator.num_pages)
        freeproject_category_post_query = freeproject_category_paginator.page(freeproject_category_paginator.num_pages)
        premium_category_post_query = premium_category_paginator.page(premium_category_paginator.num_pages)

    return {
        # context for ui
        "ui_category": ui_category,
        "ui_category_count": ui_category_count,
        "ui_category_post_query":ui_category_post_query,
        "ui_category_t3" : ui_category_t3,

         # context for backend
        "backend_category" : backend_category,
        "backend_category_count" : backend_category_count,
        "backend_category_post_query": backend_category_post_query,
        "backend_category_t3" : backend_category_t3,

         # context for algorithm
        "algorithm_category" : algorithm_category,
        "algorithm_category_count" : algorithm_category_count,
        "algorithm_category_post_query": algorithm_category_post_query,
        "algorithm_category_t3" : algorithm_category_t3,

        # context for free-projects
        "freeproject_category" : freeproject_category,
        "freeproject_category_count" : freeproject_category_count,
        "freeproject_category_post_query": freeproject_category_post_query,
        "freeproject_category_t3" : freeproject_category_t3,

        # context for premium-projects
        "premium_category" : premium_category,
        "premium_category_count" : premium_category_count,
        "premium_category_post_query": premium_category_post_query,
        "premium_category_t3" : premium_category_t3,

        # context for tips/tricks
        "tips_category" : tips_category,
        "tips_category_count" : tips_category_count,
        "tips_category_post_query": tips_category_post_query,
        "tips_category_t3" : tips_category_t3,
    }
