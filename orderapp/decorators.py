from django.http import HttpResponseForbidden

from orderapp.models import Order


def order_ownership_required(func):
    def decorated(request, *args, **kwargs):
        order = Order.objects.get(pk=kwargs['pk'])
        if not order.cafe.owner == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated


