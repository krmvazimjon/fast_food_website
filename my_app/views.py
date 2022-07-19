from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from .models import *
import requests 
from django.urls import reverse_lazy
from django.core.paginator import Paginator

class HomePageView(TemplateView):
	template_name = 'index.html'

# class BookPageView(TemplateView):
# 	template_name = 'book.html'

class AboutPageView(TemplateView):
	template_name = 'about.html'

# class MenuPageView(ListView):
# 	model = Product
# 	template_name = 'menu.html'
# 	context_object_name = 'products'

def menuPageView(request):
	if request.user.is_authenticated:
		customer = request.user
		print(request.user)
		order, created = Order.objects.get_or_create(customer = customer, complete = False)
		items = order.orderitem_set.all()
		cartItems = order.get_card_items # savatdagi mahsulotlar soni
	else:
		items = []
		order = {'get_cart_total': 0, "get_card_items": 0}
		cartItems = order['get_card_items'] # qaysi funksiya orqali hisoblasin

	obj = Product.objects.all()
	page_n = request.GET.get('page', 1)
	p = Paginator(obj, 2)
	try:
		page = p.page(page_n)
	except Exception:
		page = p.page(1)
	context = {
	'page': page,
	'cartItems': cartItems
	}
	return render(request, 'menu.html', context)

def telegram_bot_sendtext(bot_message):
	bot_token = '2085755410:AAH6uMRybPrJtOrcGLuRmgvyCEL6-FGNACU'
	bot_ChatId = '913748839'
	send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_ChatId + "&parse_mode=Markdown&text= " + bot_message
	response = requests.get(send_text)
	return response.json()



def BookPageView(request):
	if request.method == 'POST':
		name = request.POST.get('name', None)
		phone = request.POST.get('phone', None)
		email = request.POST.get('email', None)
		message = request.POST.get('message', None)
		user = Coment.objects.create(
			username = name,
			phone = phone,
			email = email,
			message = message
			)
		user.save()
		telegram_bot_sendtext(f"Ismi: {user} \nPhone:{phone} \nEmail:{email} Message:{message} ")

	return render(request = request,template_name = 'book.html')

class ProductCreateView(CreateView):
	model = Product
	template_name = 'product_create.html'
	# bu qolda qowiw fields = ('mahsulot_nomi', 'mahsulot_tarkibi','mahsulot_rasmi','mahsulot_narxi')
	fields = '__all__'
	success_url = reverse_lazy('index')

