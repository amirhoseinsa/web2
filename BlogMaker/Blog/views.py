from django.http import JsonResponse


from Blog.forms import AddPostForm, AddCommentForm
from Blog.models import Post, Blog, Comment
from members.models import UserInfo



def postg(request, bid):
    if request.method == 'GET':
        id = get_user(request)
        if id is None:
            return JsonResponse({'status': -1, 'message': 'invalid token'})
        pid = request.GET.get('id')
        p = Post.objects.filter(post_id=pid).first()
        post = {'datetime': p.time, 'id': p.post_id, 'title': p.title, 'summary': p.summary, 'text': p.text}
        res = {'status': 1, 'post': post}
        return JsonResponse(res)
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            title = form.cleaned_data['title']
            summary = form.cleaned_data['summary']
            blog = Blog.objects.filter(blog_id=bid).first()
            if blog is not None:
                post = Post.create(blog, title, summary, text)
                post.save()
                return JsonResponse({'status': 1, 'message': 'Successfully Added The Post'})



def postsg(request, blog_id):
    res = {}
    user = get_user(request)
    if user is None:
        print('invalid')
        return JsonResponse({'status': -1, 'message': 'invalid token'})
    print('In get posts', user)
    count = int(request.GET.get('count'))
    offset = int(request.GET.get('offset'))
    posts = list(Post.objects.filter(blog__blog_id=blog_id).order_by('time'))[offset:offset + count]
    res['status'] = 1
    res['posts'] = []
    for p in posts:
        temp = {'datetime': p.time, 'id': p.post_id, 'title': p.title, 'summary': p.summary}
        res['posts'].append(temp)
    return JsonResponse(res)



def commentsg(request):
    res = {}
    user = get_user(request)
    if user is None:
        return JsonResponse({'status': -1, 'message': 'invalid token'})
    post_id = request.GET.get('post_id')
    c = int(request.GET.get('count'))
    o = int(request.GET.get('offset'))
    post = Post.objects.filter(post_id=post_id).first()
    comments = list(Comment.objects.filter(post=post).order_by('time'))[o:o + c]
    res['status'] = 1
    res['comments'] = []
    for c in comments:
        temp = {'datetime': c.time, 'text': c.text}
        res['comments'].append(temp)
    return JsonResponse(res)

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
        form = AddCommentForm(request.POST)
        if form.is_valid():
            print('form is valid')
            text = form.cleaned_data['text']
            post_id = form.cleaned_data['post_id']
            post = Post.objects.filter(post_id=post_id).first()
            if post is not None:
                comment = Comment.create(post, text)
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


