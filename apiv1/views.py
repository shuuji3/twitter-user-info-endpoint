from django.http import HttpResponseRedirect, HttpResponseServerError
from apiv1.utils import resolve_user_icon_url


def user_icon(request, screen_name: str):
    img_url = resolve_user_icon_url(screen_name)
    if not img_url:
        html = '<h1>500 Server Error</h1><p>Either <b>Twitter credentials</b> or <b>screen_name</b> seems to be invalid.</p>'
        return HttpResponseServerError(html)
    return HttpResponseRedirect(img_url)
