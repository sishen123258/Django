__author__ = 'Tng'

from django.shortcuts import render
from django.core.context_processors import csrf


def search_post(request):
    ctx ={}
    ctx.update(csrf(request))
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "post.html", ctx)

