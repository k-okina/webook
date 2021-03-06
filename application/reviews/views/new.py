from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_POST
from modules.book import service as book_sv
from modules.review import service as review_sv, forms as review_form
from submodules.helper import flatten_dict_only_one_element as flatten
from django.contrib import messages
from ..urls import app_name


@require_GET
def get(request, book_pk):
    return render(request, app_name + '/new.html',
                  {'form': review_form.NewReview,
                   'hidden': {'book_pk': book_pk}})


@require_POST
def post(request, book_pk):
    """レビューを投稿する"""
    data = flatten(request.POST)
    some_params = (book_sv.get_book(book_pk), data['text'], data['star'])

    if review_sv.post_review(request.user, *some_params):
        messages.success(request, 'レビューを投稿しました!')
    else:
        messages.warning(request, '既に投稿しています!', extra_tags='danger')

    return redirect('books:detail', pk=book_pk)
