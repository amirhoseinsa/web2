from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import JsonResponse

from Blog.models import Blog
from members.forms import Form_login, Form_SignUp, Form_test
from members.models import UserInfo


def sign_up(request):
    if request.method == 'POST':
        form = Form_SignUp(request.POST)
        res = {}
        if form.is_valid():
            un = form.cleaned_data["un"]
            password = form.cleaned_data['password']
            fn = form.cleaned_data["fn"]
            ln = form.cleaned_data["ln"]
            email = form.cleaned_data['email']
            if len(password) < 5:
                res['status'] = -1
                res['message'] = 'too short password'
                return JsonResponse(res)
            if User.objects.filter(username=un).exists():
                res['status'] = -1
                res['message'] = 'user already exists'
                return JsonResponse(res)
            else:
                print("else")
            user = User.objects.create_user(un, email, password)
            user.last_name = ln
            user.first_name = fn
            blog = Blog.objects.create(owner=user, name='Home-' + user.username)
            uu = UserInfo.create_user_info(user, blog)
            user_info = uu
            res['status'] = 1
            res['message'] = 'Successfully Created User.'
            user.save()
            blog.save()
            user_info.save()
            return JsonResponse(res)
    else:
        print('Not a POST method')


def login(request):
    if request.method == 'POST':
        f = Form_login(request.POST)
        res = {}
        if f.is_valid():
            un = f.cleaned_data["un"]
            passw = f.cleaned_data['password']
            id = authenticate(request, username=un, password=passw)
            if id is not None:
                login(request, id)
                print('logged in user', id.username)
                res['status'] = 1
                token = UserInfo.objects.all().filter(user__username=un).first()
                res['token'] = token.token
                return JsonResponse(res)
            else:
                if User.objects.filter(username=un).exists():
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


def in_blog(request):
    t = request.META.__getitem__('HTTP_X_TOKEN')
    id = UserInfo.objects.filter(token=t).first()
    if id is not None:
        return id.user
    return None

def blog_idg(request):
    if request.method == 'GET':
        user = userg(request)
        if user is None:
            return JsonResponse({'status': -1, 'message': 'invalid token'})
        else :
            print("else")
        username = user.username
        blog = Blog.objects.filter(owner__username=username).first()
        res = {'blog_id': blog.blog_id, 'name': blog.name}
        return JsonResponse(res)


def userg(request):
    tt = request.META.__getitem__('HTTP_X_TOKEN')
    id = UserInfo.objects.filter(token=tt).first()
    if id is not None:
        return id.user
    else :
        print("else")
    return None


def tt(request):
    if request.method == 'POST':
        res = {'status': 1}
        print(request.META.__getitem__('HTTP_X_TOKEN'))
        form = Form_test(request.POST)
        if form.is_valid():
            print('Its valid')
            post_id = form.cleaned_data["id_p"]
            text = form.cleaned_data['text']
            title = form.cleaned_data['title']
            print(post_id, text, title)
        return JsonResponse(res)

