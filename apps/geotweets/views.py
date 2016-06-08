from django.shortcuts import render
from django.conf import settings
from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
def index(request):

    d = dict(title="A Billion Streaming GeoTweets",
            contributor="Harvard Center for Geographic Analysis")
    return render(request, 'index.html', d)

@xframe_options_exempt
def open_layers_test(request):

    d = dict(title="A Billion Streaming GeoTweets",
            contributor="Harvard Center for Geographic Analysis")
    return render(request, 'ol_test_02.html', d)
