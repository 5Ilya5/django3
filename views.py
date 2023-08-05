def profile(request):
    user_orders = Order.objects.filter(user=request.user)
    user_order_item = OrderItem.objects.all()

    data = {
        'user_orders': user_orders,
        'user_order_item': user_order_item,
    }
    return render(request, 'store/main_pages/profile.html', data)