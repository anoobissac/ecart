from unicodedata import category
from django.shortcuts import render,redirect
from django.db.models import Q, F
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,View
from product.models import ProductModel,CategoryModel
from product.forms import ProductForm,CategoryForm

# Create your views here.
#class ProductCreateView(CreateView):
#    template_name="products/create.html"
#    model=ProductModel
#    #fields = ['name','price','image','description','category','unit']
#    form_class=ProductForm
#    success_url = reverse_lazy('product_list')

class ProductListView(ListView):
    template_name='products/list.html'
    model=ProductModel


class ProductDetailView(DetailView):
    template_name='products/detail.html'
    model=ProductModel

class ProductUpdateView(UpdateView):
    template_name="products/update.html"
    model=ProductModel
    #fields = ['name','price','image','description','category','unit']
    form_class=ProductForm
    success_url = reverse_lazy('product_list')

class ProductDeleteView(DeleteView):
    template_name="products/delete.html"
    model=ProductModel    
    success_url = reverse_lazy('product_list')


#Category View
class CategoryCreateView(CreateView):
    template_name="products/category/create.html"
    model=CategoryModel
    fields = ['name']
    success_url = reverse_lazy('category_list')

class CategoryListView(ListView):
    template_name='products/category/list.html'
    model=CategoryModel

class CategoryDetailView(DetailView):
    template_name='products/category/detail.html'
    model=CategoryModel

class CategoryUpdateView(UpdateView):
    template_name="products/category/update.html"
    model=CategoryModel
    fields = ['name']
    success_url = reverse_lazy('category_list')

class CategoryDeleteView(DeleteView):
    template_name="products/category/delete.html"
    model=CategoryModel    
    success_url = reverse_lazy('category_list')

class ProductListByCategory(View):
    template_name='products/searchlist.html'
    def get(self,request,pk):
        
        context={ 'product_list':ProductModel.objects.filter(category__id=pk)}
        return render(request,self.template_name,context)


class SearchView(View):
    template_name = 'products/searchlist.html'
    def get(self, request):
        query = request.GET.get('query')
        products = ProductModel.objects.filter(
            Q(name__icontains=query) | Q(category__name__icontains=query)
        )
        context = {
            'product_list': products
        }
        return render(request, self.template_name, context)

class ProductCreateView(View):
    template_name="products/create.html"
    model=ProductModel
    form_class=ProductForm
    success_url = reverse_lazy('product_list')
    def get (self,request):
        
        context={
            'form':self.form_class()
        }
        return render (request,self.template_name, context)
    
    def post (self, request):
        files=self.request.FILES
        form=self.form_class(request.POST,request.FILES)
        if form.is_valid():
            self.form_valid(form)
        else:
            return self.form_invalid(form)
        return self.get_success_url()

    def form_valid(self, form):
        form.save()

    def form_invalid(self, form):
        context={
            form:self.form_class(form)
        }
        return render(self.request,self.template_name,context)
    
    def get_success_url(self):
        return redirect(self.success_url)

class AddToCartView(View):
    template_name="products/addtocart.html"
    model=ProductModel
