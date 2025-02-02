from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, TemplateView
from .models import Product, Order

class ProductListView(ListView):
    model = Product
    template_name = 'shop/product_list.html'
    context_object_name = 'products'
    paginate_by = 9

    def get_queryset(self):
        return Product.objects.filter(available=True).order_by('-created_at')

class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product_detail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_products'] = Product.objects.filter(
            available=True
        ).exclude(id=self.object.id)[:4]
        return context

class CartView(TemplateView):
    template_name = 'shop/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            order, created = Order.objects.get_or_create(
                user=self.request.user,
                completed=False
            )
            context['order'] = order
        return context

def add_to_cart(request, product_id):
    if not request.user.is_authenticated:
        return redirect('account_login')
    
    product = get_object_or_404(Product, id=product_id)
    order, created = Order.objects.get_or_create(
        user=request.user,
        completed=False
    )
    order.products.add(product)
    return redirect('shop:cart')