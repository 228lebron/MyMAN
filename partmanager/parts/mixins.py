class UserContextMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_sale'] = 'sale' in self.request.user.groups.values_list('name', flat=True)
        context['is_product_man'] = 'product' in self.request.user.groups.values_list('name', flat=True)
        return context