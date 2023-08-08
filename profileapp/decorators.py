from profileapp.models import Profile
from django.http import HttpResponseForbidden

def profile_ownership_required(func):
    def decorated(request, *args, **kwargs):
        profile = Profile.objects.get(pk=kwargs['pk'])
        if not profile == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated

