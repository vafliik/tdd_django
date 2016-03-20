from django.shortcuts import render, redirect

from lists.models import Item,List

def home_page(request):
	items = Item.objects.all()
	return render(request, 'home.html', {'items': items}) 

def new_list(request):
	list_ = List.objects.create()
	new_item_text = request.POST['item_text']
	Item.objects.create(text=new_item_text,list=list_)
	return redirect('/lists/%d/' % (list_.id,))

def list_view(request,list_id):
	list_ = List.objects.get(id=list_id)
	items = Item.objects.filter(list=list_)
	return render(request, 'lists.html', {'items': items, 'list': list_}) 

def add_item(request,list_id):
	list_ = List.objects.get(id=list_id)
	new_item_text = request.POST['item_text']
	Item.objects.create(text=new_item_text,list=list_)
	return redirect('/lists/%d/' % (list_.id))
