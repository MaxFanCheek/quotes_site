import random
from .models import Quote
from django.db.models import Sum

def weighted_random_quote():
    qs = Quote.objects.all()
    total = qs.aggregate(Sum('weight'))['weight__sum'] or 1
    point = random.randrange(1, total + 1)
    acc = 0
    for q in qs:
        acc += q.weight
        if acc >= point:
            return q
