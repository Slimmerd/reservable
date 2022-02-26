# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST

from backend.clients.models import Clients
from backend.merchants.models import Merchants
from backend.order_items.models import OrderItems
from backend.orders.models import Orders


@require_GET
def getOrder(request, atr):
    order = Orders.objects.get(id=atr)

    return JsonResponse({'id': order.id,
                         'merchantID': order.merchant_id,
                         'persons': order.persons,
                         'isReservation': order.is_reservation,
                         'reservedDate': order.reserved_date,
                         'orderItems': order.orderitems_set.get(),
                         'comments': order.comment,
                         'orderReservationCost': order.reservation_cost,
                         'orderTotal': order.total,
                         'createdAt': order.created_at
                         })


@require_GET
@login_required
def getOrderMerchant(request, atr):
    order = Orders.objects.get(id=atr)

    return JsonResponse({'order': order, 'items': order.orderitems_set.get(), 'client': order.client.get()})


@require_POST
def createOrder(request):
    if 'client' or 'order' not in request.POST:
        return JsonResponse({'error': 'Incorrect POST parameters'})

    input_client = request.POST['client']
    input_order = request.POST['order']

    if not input_client or not input_order:
        return JsonResponse({'error': 'Fields cannot be empty'})

    merchant = Merchants.objects.get(id=input_order.id)

    new_client = Clients(
        name=input_client.name,
        email=input_client.email,
        phone=input_client.phone,
    )
    new_client.save()

    new_order = Orders(
        is_reservation=input_order.isReservation,
        reserved_date=input_order.reservedDate,
        persons=input_order.persons,
        percent=merchant.percent,
        reservation_cost=merchant.reservation_cost,
        total=input_order.total,
        total_after_percent=input_order.total - (input_order.total * (merchant.percent / 100)),
        comment=input_order.comment,
        merchant=merchant,
        client=new_client,
    )
    new_order.save()

    for item in input_order.orderItems:
        new_order_items = OrderItems(
            name=item.name,
            price=item.price,
            quantity=item.quantity,
            order=new_order,
        )
        new_order_items.save()

    return JsonResponse({'success': 'Product successfully added'})
