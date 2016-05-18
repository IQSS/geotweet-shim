from django.shortcuts import render

def index(request):

    d = dict(title="A Billion Streaming GeoTweets",
            contributor="Harvard Center for Geographic Analysis")
    return render(request, 'index.html', d)


def open_layers_test(request):

    d = dict(title="A Billion Streaming GeoTweets",
            contributor="Harvard Center for Geographic Analysis")
    return render(request, 'ol_test_02.html', d)
