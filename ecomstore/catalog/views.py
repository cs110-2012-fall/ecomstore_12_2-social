from django.shortcuts import get_object_or_404, render_to_response
from ecomstore.catalog.models import Category, Product
from django.template import RequestContext

from django.core import urlresolvers
from ecomstore.cart import cart
from django.http import HttpResponseRedirect
from ecomstore.catalog.forms import ProductAddToCartForm

def index(request, template_name="catalog/index.html"):
    """ site home page """
    page_title = 'Modern Musician | Musical Instruments and Sheet Music for Musicians'
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

def show_category(request, category_slug, template_name="catalog/category.html"):
    """ view for each individual category page """
    c = get_object_or_404(Category, slug=category_slug)
    count = 0
    products = c.product_set.all()
    page_title = c.name
    meta_keywords = c.meta_keywords
    meta_description = c.meta_description   
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

def show_product(request, product_slug, template_name="catalog/product.html"):
    p = get_object_or_404(Product, slug=product_slug)
   # imageList = []
   # if p.image2 and p.thumbnail2:
   #    imageList.append(p.image2)
   #     imageList.append(p.thumbnail2)
   # if p.image3 and p.thumbnail3:
   #     imageList.append(p.image3)
   #     imageList.append(p.thumbnail3)
   # if p.image4 and p.thumbnail4:
   #     imageList.append(p.image4)
   #     imageList.append(p.thumbnail4)
        
    categories = p.categories.filter(is_active=True)
    page_title = p.name
    meta_keywords = p.meta_keywords
    meta_description = p.meta_description
    if request.method == "POST":
		postdata = request.POST.copy()
		form = ProductAddToCartForm(request,postdata)
		if form.is_valid():
			cart.add_to_cart(request)
			if request.session.test_cookie_worked():
				request.session.delete_test_cookie()
			url = urlresolvers.reverse('show_cart')
			return HttpResponseRedirect(url)
    else:
        #create the unbound form. Notice the request as a keyword argument
        form = ProductAddToCartForm(request=request, label_suffix=':')
    # assign the hidden input the product slug
    	form.fields['product_slug'].widget.attrs['value'] = product_slug
    # set test cookie to make sure cookies are enabled
    	request.session.set_test_cookie()    
    	return render_to_response(template_name, locals(), context_instance=RequestContext(request))

