from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST

from .models import Products
from ..merchants.models import Merchants


@require_GET
def getProduct(request):
    products = Products.objects.values()
    return JsonResponse({'products': list(products)})


@require_POST
@login_required
def createProduct(request):
    if 'name' or 'price' or 'description' not in request.POST:
        return JsonResponse({'error': 'Incorrect POST parameters'})

    input_name = request.POST['name']
    input_description = request.POST['description']
    input_price = request.POST['price']

    if not input_price or not input_name or not input_description:
        return JsonResponse({'error': 'Fields cannot be empty'})

    new_product = Products(name=input_name, description=input_description, price=input_price)
    new_product.save()

    return JsonResponse({'success': 'Product successfully added'})


@require_POST
@login_required
def editProduct(request, pk):
    product = Products.objects.get(id=pk)
    merchant = Merchants.objects.get(id=product.merchant_id)

    if request.user != merchant.owner_id:
        return JsonResponse({'error': 'Server Internal Error'})
    # todo add update product
    try:
        Products.objects.update()
    except:
        return JsonResponse({'error': ''})


@require_POST
@login_required
def deleteProduct(request, pk):
    product = Products.objects.get(id=pk)
    merchant = Merchants.objects.get(id=product.merchant_id)

    if request.user != merchant.owner_id:
        return JsonResponse({'error': 'Server Internal Error'})
