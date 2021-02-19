from django.shortcuts import render

# Create your views here.
from ecommerce.forms import OrderForm


def make_order(request, pk):
    order_form = OrderForm()

    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order= order_form.save(commit=False)
            order.user_id = pk

    context = {
        'order_form': order_form
    }

    return render(request=request, template_name='order/make_order.html', context=context)



