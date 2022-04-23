from django.shortcuts import render, redirect

# Create your views here.

def view_bag(request):
    """ A view to return the bag contents page"""

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ 
    Add a quantitiy of the specified product to the shopping bag
    by submitting the form to this view including product_id and 
    quantity. The view will get bag variable if it exists in current
    session or create if it doesn't exist and add the items to the bag
    or update the quantity if it already exists and overwrite variable
    session with updated version
    """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)