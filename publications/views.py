"""views publications"""

# Django
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

publications = [
    {
        'user' : {
            'photo' : 'https://i.picsum.photos/id/1/5616/3744.jpg?hmac=kKHwwU8s46oNettHKwJ24qOlIAsWN9d2TtsXDoCWWsQ',
            'username': 'santiago18',
        },
        'publication' : {
            'picture' : 'https://i.picsum.photos/id/1054/3079/1733.jpg?hmac=Rk5_Xt3oLlDLJHH3ZDyHCqua0s45mhNjXmID277ZOMI',
            'info' : ['info1','info2','info3','info4'],
            'description' : 'Esta es una imagen de unos apartamentos hechos mierda'
        }
    },
        {
        'user' : {
            'photo' : 'https://i.picsum.photos/id/1083/5472/3648.jpg?hmac=CtOxgXc6Oe3TQvKBXtPsKVT9Z2Yg7SJKWVlgWPeMBUs',
            'username': 'Maria7',
        },
        'publication' : {
            'picture' : 'https://i.picsum.photos/id/1074/5472/3648.jpg?hmac=w-Fbv9bl0KpEUgZugbsiGk3Y2-LGAuiLZOYsRk0zo4A',
            'info' : ['info1','info2','info3','info4'],
            'description' : 'Esta es la imagen de un hermoso leon'
        }
    }
]

def view_publications(request):
    return render(request,'publications/list.html',{'publications':publications})