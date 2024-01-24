from django.shortcuts import render

# Create your views here.
def index(request):
    posts = [{"author": "Jimmy", "contents": "I am the coolest!"},
                  {"author": "Samiha", "contents": "I am even cooler!"}]
    return render(request, 'index.html', {"blog_posts": posts})

def post_create(request):
    # TODO: add logic that handles requests to create new posts
    pass

def post_delete(request):
    # TODO: add logic that handles requests to delete posts
    pass

def post_edit(request):
    # TODO: add logic that handles requests to edit posts
    pass