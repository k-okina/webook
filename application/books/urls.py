from django.urls import path
from submodules.helper import ViewRouter

app_name = 'books'

route = ViewRouter(app_name=app_name)

urlpatterns = [
    # 一覧画面
    path('', route.index, name='index'),

    # 詳細画面
    path('<int:pk>', route.detail, name='detail'),

    # 新規登録画面
    path('new', route.new, name='new'),

    # 新規登録画面
    path('<int:pk>/buy', route.buy, name='buy'),
]
