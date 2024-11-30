from django.shortcuts import render


def get_home(requests):
    return render(
        request=requests,
        template_name='guides/index.html',
        context={}
    )
