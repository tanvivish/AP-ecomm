def layout(request):
	return render(request, 'layout.html')

def products(request):
    products = Product.find_all()
    brands = Brand.find_all()
    categories = Category.find_all()
    featured = Collection.find_by_name("featured")
    cart = ShoppingCart.get()
    return render(request, "shop/products.html", {"brands": brands, "categories": categories, "products": products,
                                             "featured": featured, "cart": cart})
