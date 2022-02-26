from django.urls import path
from .views import (demo_view,
                    demo_view_2,
                    demo_view_3,
                    demo_view_4)

urlpatterns = [
    path('demo-url/', demo_view, name='demo_view'),
    path('demo-url-2/', demo_view_2, name='demo_view_2'),
    path('demo-url-3/', demo_view_3, name='demo_view_3'),
    path('demo-url-4/', demo_view_4, name='demo_view_4'),
]
