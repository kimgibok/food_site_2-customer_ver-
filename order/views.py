from django.shortcuts import render
from seller.models import Food
from .models import Cart
from django.db.models import Sum

# Create your views here.
def order_detail(request, pk):
    food = Food.objects.get(pk=pk)
    context = {
        'object':food
    }
    return render(request, 'order/order_detail.html', context)

from django.http import JsonResponse
def modify_cart(request):
    # 어떤 음식(food_id)에 amount를 amountChange만큼 변경하고 <- 개발하기
    user = request.user
    food_id= request.POST['foodId']
    food = Food.objects.get(pk=food_id)
    cart, _ = Cart.objects.get_or_create(user=user, food=food) 
    cart.amount+=int(request.POST['amountChange'])
    if cart.amount>0:
        cart.save()
    totalcount = user.cart_set.aggregate(total=Sum('amount'))['total']
    # 변경된 최종 결과를 반환(JSON)
    context = {
        'newQuantity':cart.amount, 
        'totalQuantity' : totalcount,
        'message':'수량이 성공적으로 업데이트 되었습니다.',
        'success':True
    }
    return JsonResponse(context)