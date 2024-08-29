from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import User, AuctionList, Link, Comment
from datetime import datetime

CATEGORIES = ["Non-category", "Electronic", "Special Metal", "Universe", "Magic"]


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
     

def index(request):
    products = AuctionList.objects.all()
    return render(request, "auctions/index.html", {
        "products": products
    })

def category(request):
    category = "All"
    products = AuctionList.objects.all()

    if request.method == "POST":
        category = request.POST.get("category")
    
    if category != "All" and category in CATEGORIES:
        products = products.filter(category=category)

    return render(request, "auctions/category.html", {
        "categories": CATEGORIES,
        "products": products,
        "category": category
    })

def create(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        description = request.POST.get("description")
        category = request.POST.get("category")
        price = request.POST.get("price")
        image_url = request.POST.get("image_url")
        username = request.user
        

        now = datetime.now()
        time = f"Created {now.day}/{now.month}/{now.year}, {now.hour}:{now.minute}"

        items = AuctionList(title=title, description=description, category=category, image_url=image_url, time=time, price=price)
        items.save()

        
        p = Link(product=items, person=username, isActive=True)
        p.save()
        return index(request)
    
    return render(request, "auctions/create.html", {
        "categories": CATEGORIES
    })

def specific(request, auction_id):
    product = AuctionList.objects.get(id=auction_id)
    username = request.user
    count = Link.objects.filter(product=product).count() - 1
    creater = Link.objects.filter(product=product, isActive=True).first()
    link = Link.objects.filter(product=product, person=username).first()
    highest_bidder = Link.objects.filter(product=product, bid=product.price).first()
    comments = product.product_comment.all()

    if not link:
        link = Link(product=product, person=username)

    if request.method == "POST": 

        if "close" in request.POST:
            product.closed = True
            product.save()

        elif "comment" in request.POST:
            comment = request.POST.get("comment_product")
            Cmt = Comment(product=product, person=username, comment=comment)
            Cmt.save()

        elif "add_watchlist" in request.POST:
            link.watchList = True
            link.save()

        elif "remove_watchlist" in request.POST:  
            link.watchList = False
            link.save()

        elif "place_bid" in request.POST:
            bid = request.POST.get("bid")
            if bid and ((count == 0 and float(bid) >= product.price) or (count > 0 and float(bid) > product.price)):
                link.bid = bid 
                link.save()
                product.price = bid
                product.save()
            else:
                return HttpResponse("Invalid bid")
            
        return HttpResponseRedirect(reverse("specific", args=[product.id]))
    

    return render(request, "auctions/specific_auction.html", {
        "product": product,
        "creater": creater,
        "count": count,
        "link": link,
        "highest_bidder": highest_bidder,
        "comments_product": comments
    })


def watchlist(request):
    username = request.user
    
    link_products = username.person_link.filter(watchList=True)

    products = [link.product for link in link_products]

    return render(request, "auctions/watchlist.html", {
        "products": products       
    })
