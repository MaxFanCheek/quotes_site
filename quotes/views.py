from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import F
from .models import Quote
from .services import weighted_random_quote

def random_quote(request):
    q = weighted_random_quote()
    Quote.objects.filter(pk=q.pk).update(views=F('views') + 1)

    if request.method == 'POST':
        field = 'likes' if 'like' in request.POST else 'dislikes'
        Quote.objects.filter(pk=q.pk).update(**{field: F(field) + 1})
        return redirect('random')

    return render(request, 'quotes/random.html', {'quote': q})


from django.db.models import IntegerField, Value, ExpressionWrapper

def top_quotes(request):
    top = (Quote.objects
                 .annotate(score=F('likes') - F('dislikes'))
                 .order_by('-score', '-likes')[:10])
    return render(request, 'quotes/top.html', {'quotes': top})
