class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='orders', verbose_name='Заказы',
                             default=1)
    username = models.CharField(max_length=50, verbose_name='Имя пользователя')
    email = models.EmailField()
    vk_or_telegram = models.CharField(max_length=255, verbose_name='Ссылка для связи', default='vk.com')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False, verbose_name='Оплачено')

    class Meta:
        ordering = ['-created',]
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


    def __str__(self):
        return 'Заказ {}'.format(self.id)


    def get_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order', on_delete=models.CASCADE)
    product = models.ForeignKey(Posts, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price