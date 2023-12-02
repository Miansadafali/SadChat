
def user_logined(request):
    return {'logined_user': request.user}