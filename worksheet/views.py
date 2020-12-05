
import random
import collections

from mathswithella import question

from django.core.paginator import Paginator
from django.shortcuts import render

from worksheet.models import Worksheet, WorksheetPage, WorksheetPageQuestion
from question.models import QuestionTemplate

def index(request):
    return render(request, 'worksheet/index.html')

def detail(request, internal_name, page_num):
    worksheet = Worksheet.objects.get(internal_name=internal_name)
    pages = worksheet.worksheetpage_set.all()

    print(pages)

    page_structure = {}
    for i in range(len(pages)):
        page_structure[pages[i].number] = pages[i].worksheetpagequestion_set.all()

    print(max(page_structure.keys()))

    context = {
        'page_structure': page_structure,
        'page_last': max(page_structure.keys()),
        'internal_name': internal_name,
        'active_page_num': page_num,
    }
    return render(request, 'worksheet/detail.html', context)