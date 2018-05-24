from django.http import HttpResponseRedirect
from apiv1.utils import resolve_user_icon_url


def user_icon(request, screen_name: str):
    img_url = resolve_user_icon_url(screen_name)
    return HttpResponseRedirect(img_url)
