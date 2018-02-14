from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from constants import ROOT_NAME
from submodules.helper import get_urls
from accounts import urls as account_urls
from books import urls as book_urls
from index import urls as index_urls
from categories import urls as category_urls
from settings import MEDIA_ROOT, DEBUG
from django.urls import re_path
from django.views.static import serve

urlpatterns = [
    url('', get_urls(index_urls)),
    path('admin/', admin.site.urls),
    path('accounts/', get_urls(account_urls)),
    path('books/', get_urls(book_urls)),
    path('categories/', get_urls(category_urls)),
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': MEDIA_ROOT,
    }),
]
