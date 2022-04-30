from django.shortcuts import render
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KuCSCDpnCSWalL7UOv6wmtsBmRT88dCPw9jnN1YQ35SoA4VDL6lA5Lj8ZjRmqYMA6Dz4WryQN9MyDGsjPRo9ZYI00037EH2FF',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
