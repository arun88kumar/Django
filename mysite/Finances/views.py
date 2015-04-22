from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Expense, Income


def index(request):
    exp_list = Expense.objects.all()
    inc_list = Income.objects.all()

    exp_page = Paginator(exp_list, 10)
    page = request.GET.get('page')
    try:
        exps = exp_page.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        exps = exp_page.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        exps = exp_page.page(exp_page.num_pages)

    inc_page = Paginator(inc_list, 10)
    page = request.GET.get('page')
    try:
        incs = inc_page.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        incs = inc_page.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        incs = inc_page.page(inc_page.num_pages)

    context = {'expenses': exps, 'income': incs}
    return render(request, 'Finances/index.html', context)
