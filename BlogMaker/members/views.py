from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import JsonResponse

from Blog.models import Blog
from members.forms import SignIn, SignUp, TestForm
from members.models import UserInfo

# todo Upload images.


def login(request):
    if request.method == 'POST':
        f = SignIn(request.POST)
        res = {}
        if f.is_valid():
            username = f.cleaned_data['username']
            passw = f.cleaned_data['password']
            id = authenticate(request, username=username, password=passw)
            if id is not None:
                login(request, id)
                print('logged in user', id.username)
                res['status'] = 1
                token = UserInfo.objects.all().filter(user__username=username).first()
                res['token'] = token.token
                return JsonResponse(res)
            else:
                if User.objects.filter(username=username).exists():
                    res['status'] = -1
                    res['message'] = 'wrong password'
                else:
                    res['status'] = -1
                    res['message'] = 'user not found'
            return JsonResponse(res)
        else:
            res['status'] = -1
            res['message'] = 'Form is Not valid'
            return JsonResponse(res)

    else:
        print('Not a POST method')



def blog_idg(request):
    if request.method == 'GET':
        user = userg(request)
        if user is None:
            return JsonResponse({'status': -1, 'message': 'invalid token'})
        username = user.username
        blog = Blog.objects.filter(owner__username=username).first()
        res = {'blog_id': blog.blog_id, 'name': blog.name}
        return JsonResponse(res)


def userg(request):
    tt = request.META.__getitem__('HTTP_X_TOKEN')
    id = UserInfo.objects.filter(token=tt).first()
    if id is not None:
        return id.user
    return None


def tt(request):
    if request.method == 'POST':
        res = {'status': 1}
        print(request.META.__getitem__('HTTP_X_TOKEN'))
        form = TestForm(request.POST)
        if form.is_valid():
            print('Its valid')
            post_id = form.cleaned_data['post_id']
            text = form.cleaned_data['text']
            title = form.cleaned_data['title']
            print(post_id, text, title)
        return JsonResponse(res)

def sign_up(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        res = {}
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            if User.objects.filter(username=username).exists():
                res['status'] = -1
                res['message'] = 'user already exists'
                return JsonResponse(res)
            if len(password) < 5:
                res['status'] = -1
                res['message'] = 'too short password'
                return JsonResponse(res)
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            blog = Blog.objects.create(owner=user, name='Home-' + user.username)
            user_info = UserInfo.create_user_info(user, blog)
            res['status'] = 1
            res['message'] = 'Successfully Created User.'
            user.save()
            blog.save()
            user_info.save()
            return JsonResponse(res)
    else:
        print('Not a POST method')
