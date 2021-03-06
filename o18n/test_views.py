import json

# JsonResponse is available in Djnago 1.7+
from django.http import HttpResponse


UNSERIALIZABLE_ATTRS = {'environ', 'META', 'resolver_match'}


def info(request):
    request = {k: v for k, v in request.__dict__.items()
                    if not (k.startswith('_') or k in UNSERIALIZABLE_ATTRS)}
    return HttpResponse(json.dumps(request), content_type='application/json')
