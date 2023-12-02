from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from friendlists.models import FriendRequest

User = get_user_model()
# Create your views here.
@login_required(login_url='/login/')
def index(request):
    friend_requests = FriendRequest.objects.filter(to_user=request.user).select_related('from_user')

    users = User.objects.exclude(id=request.user.id)
    friend_requests = FriendRequest.objects.filter(to_user=request.user)
    friend_requests_sent = FriendRequest.objects.filter(from_user=request.user)
    
    users_with_requests = [request.from_user for request in friend_requests]
    users_with_requests_sent = [request.to_user for request in friend_requests_sent]
    
    user_request_ids = {}
    for user in users:
        for request in friend_requests:
            if request.from_user == user:
                user_request_ids[user] = request.id
                break
            
    context = {
        'users': users,        
        'users_with_requests': users_with_requests,
        'users_with_request_sent': users_with_requests_sent,
        'user_request_ids': user_request_ids,
    }
    
    return render(request, 'pages/default-member.html', context)


@login_required(login_url='/login/')
def request_friendship(request, recipient_id):
    if request.method == 'POST':
        recipient = get_object_or_404(User, id=recipient_id)
        FriendRequest.objects.get_or_create(
            from_user=request.user,
            to_user=recipient)
        print("this is the user : " + recipient.username)
        return redirect('index')
    else:
        return redirect('index')
    
    
@login_required(login_url='/login/')
def accept_friendship(request, user_id):
    if request.method == 'POST':
        from_user = get_object_or_404(User, id=user_id)
        request = get_object_or_404(FriendRequest, from_user=from_user, to_user=request.user)
        request.accept()
        return redirect('index')
    else:
        return redirect('index')