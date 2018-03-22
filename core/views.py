from django.shortcuts import render


def hi(requset, w, c):
    # w= requset.GET.get('w')
    # return HttpResponse('<h1>{}</h1>'.format(w+c))
    s = w + c
    return render(requset, "hi.html", {
        "s": s,
    })


def r(request, start, stop):
    if start > stop:
        start, stop = stop, start
    rr = range(start, stop + 1)
    rr = reversed(rr)

    return render(request, "r.html", {
        'rr': rr,
    })


def tag_test(request):
    ll = [1, 2, 3, 4, 5, 6, 7, 8]
    return render(request, 'tag_test.html', {
        'll': ll
    })
