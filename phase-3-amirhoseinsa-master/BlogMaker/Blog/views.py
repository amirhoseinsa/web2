from django.http import JsonResponse


from Blog.forms import Form_AddP, Form_AddC
from Blog.models import BlogPosts, Blog, PostComments
from members.models import UserInfo



def postg(request, bid):
    if request.method == 'GET':
        id = get_user(request)
        if id is None:
            return JsonResponse({'status': -1, 'message': 'invalid'})
        pid = request.GET.get('id')
        p = BlogPosts.objects.filter(post_id=pid).first()
        post = {'datetime': p.time, 'id': p.post_id, 'title': p.title, 'summary': p.summary, 'text': p.text}
        res = {'status': 1, 'post': post}
        #print(res)
        return JsonResponse(res)
    if request.method == 'POST':
        form = Form_AddP(request.POST)
        if form.is_valid():
            s = form.cleaned_data['summary']
            t = form.cleaned_data['text']
            t2 = form.cleaned_data['title']
            blog = Blog.objects.filter(blog_id=bid).first()
            if blog is not None:
                post = BlogPosts.create(blog, t2, s, t)
                post.save()
                return JsonResponse({'status': 1, 'message': 'Successfully Added'})


def commentsg(request):
    res = {}
    user = get_user(request)
    if user is None:
        return JsonResponse({'status': -1, 'message': 'invalid token'})
    post_id = request.GET.get('post_id')
    c = int(request.GET.get('count'))
    o = int(request.GET.get('offset'))
    post = BlogPosts.objects.filter(post_id=post_id).first()
    comments = list(PostComments.objects.filter(post=post).order_by('time'))[o:o + c]
    res['status'] = 1
    res['comments'] = []
    for c in comments:
        temp = {'datetime': c.time, 'text': c.text}
        res['comments'].append(temp)
    return JsonResponse(res)


def postsg(request, blog_id):
    res = {}
    user = get_user(request)
    if user is None:
        print('invalid')
        return JsonResponse({'status': -1, 'message': 'invalid'})
    print('In get posts', user)
    c = int(request.GET.get('count'))
    o = int(request.GET.get('offset'))
    p = list(BlogPosts.objects.filter(blog__blog_id=blog_id).order_by('time'))[o:o + c]
    res['status'] = 1
    #print(res)
    res['posts'] = []
    for p in p:
        temp = {'datetime': p.time, 'id': p.post_id, 'title': p.title, 'summary': p.summary}
        res['posts'].append(temp)
    return JsonResponse(res)


def comment_c(request):
    if request.method == 'POST':
        u = get_user(request)
        if u is None:
            return JsonResponse({'status': -1, 'message': 'invalid'})
        f = Form_AddC(request.POST)
        if f.is_valid():
            print('form is valid')
            text = f.cleaned_data['text']
            post_id = f.cleaned_data["id_p"]
            post = BlogPosts.objects.filter(post_id=post_id).first()
            if post is not None:
                comment = PostComments.create(post, text)
                comment.save()
                print(comment)
                ans = {'status': 1}
                tmp = {'text': text, 'datetime': comment.time}
                ans['comment'] = tmp
                print(ans)

                return JsonResponse({'status': 1, 'comment': ans})
        else:
            print('form is not valid')
    return JsonResponse({'status': -1, 'message': 'Under Construction'})




def get_user(request):
    t = request.META.__getitem__('HTTP_X_TOKEN')
    id = UserInfo.objects.filter(token=t).first()
    if id is not None:
        return id.user
    return None

# post_id text POST
def comment_c(request):
    if request.method == 'POST':
        user = get_user(request)
        if user is None:
            return JsonResponse({'status': -1, 'message': 'invalid token'})
        form = Form_AddC(request.POST)
        if form.is_valid():
            print('form is valid')
            text = form.cleaned_data['text']
            post_id = form.cleaned_data["id_p"]
            post = BlogPosts.objects.filter(post_id=post_id).first()
            if post is not None:
                comment = PostComments.create(post, text)
                comment.save()
                print(comment)
                ans = {'status': 1}
                temp = {'text': text, 'datetime': comment.time}
                ans['comment'] = temp
                print(ans)

                return JsonResponse({'status': 1, 'comment': ans})
        else:
            print('form is not valid')
    return JsonResponse({'status': -1, 'message': 'Under Construction'})


