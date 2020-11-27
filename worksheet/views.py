
import random

from mathswithella import question

from django.core.paginator import Paginator
from django.shortcuts import render

from worksheet.models import Worksheet

def index(request):
    return render(request, 'worksheet/index.html')

def detail(request, worksheet_internal_name, page_num):
    w = Worksheet.objects.get(internal_name=worksheet_internal_name)
    qs = w.question_set.all()

    questions = []
    for q in qs:
        qt = q.question_template
        questions.append({
            'number': q.number,
            'template': 'worksheet/templates/%s' % qt.template_name,
            'detail': getattr(question, qt.internal_name),
        })
    
    p = Paginator(questions, 3)

    print(questions)

    context = {
        'worksheet_internal_name': worksheet_internal_name,
        'questions': p.page(page_num),
        'pagination': {
            'range': p.page_range,
            'number': page_num,
            'count': p.num_pages,
        }
    }
    return render(request, 'worksheet/detail.html', context)