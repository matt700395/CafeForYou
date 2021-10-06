from django.http import HttpResponseForbidden

from cafeapp.models import Cafe


def cafe_ownership_required(func):
    def decorated(request, *args, **kwargs):
        cafe = Cafe.objects.get(pk=kwargs['pk'])
        if not cafe.owner == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated