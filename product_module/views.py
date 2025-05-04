from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from product_module.models import Product, ProductComment, ProductCategories, ProductCategoriesMain


# Create your views here.


class ProductListView(ListView):
    model = Product
    template_name = 'product_module/product_list.html'
    context_object_name = 'products'
    paginate_by = 8
    
    def get_queryset(self):
        query = super().get_queryset()
        category_name = self.kwargs.get('category')
        main_category_name = self.kwargs.get('main_category')
        if category_name is not None:
            query = query.filter(category__url_title__iexact=category_name)
        elif main_category_name is not None:
            query = query.filter(main_category__url_title__iexact=main_category_name)
        return query


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        product: Product = kwargs.get('object')
        context['comments'] = ProductComment.objects.filter(success=True, product_id=product.id,
                                                            parent_id=None).order_by('-shamsi_date').prefetch_related('productcomment_set')

        return context


def send_product_comment(request):
    if request.user.is_authenticated:
        product_comment = request.GET.get('productComment')
        product_parent = request.GET.get('parentId')
        product_id = request.GET.get('productId')
        new_comment = ProductComment(product_id=product_id, comment=product_comment, parent_id=product_parent,
                                     user_id=request.user.id)
        new_comment.save()
        return HttpResponse('success')


def product_category_component(request):
    context = {
        'main_categories': ProductCategories.objects.filter(is_active=True),
    }
    return render(request, 'product_module/components/product_category_component.html', context)


def product_main_category_component(request):
    context = {
        'categories_mother': ProductCategoriesMain.objects.filter(is_active=True),
    }
    return render(request, 'product_module/components/product_main_category_component.html', context)


def search(request):
    if request.method == 'POST':
        query_name = request.POST.get('search_input')
        if query_name:
            result_1 = Product.objects.filter(title__contains=query_name)
            result_2 = Product.objects.filter(brand__contains=query_name)
            result_3 = Product.objects.filter(stalk__contains=query_name)
            result = result_1 | result_2 | result_3
            context = {
                'products': result
            }
            return render(request, 'product_module/product_list.html', context)
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'product_module/product_list.html', context)
