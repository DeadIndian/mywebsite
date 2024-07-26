from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList

# Create your views here.
def index(response,id):
	ls = ToDoList.objects.get(id = id)

	if ls in response.user.todolist.all():		

		if response.method == "POST":
			print(response.POST)
			if response.POST.get("save"):
				for item in ls.item_set.all():
					if response.POST.get("c" + str(item.id)) == "clicked":
						item.complete = True
					else:
						item.complete = False

					item.save()

			elif response.POST.get("newItem"):
				print("uhm")
				txt = response.POST.get("new")
				
				if len(txt) > 2:
					
					ls.item_set.create(text=txt, complete = False)
				else:
					print("invalid")

			elif response.POST.get("edit"):
				return HttpResponseRedirect("/edit/%i" %id)

			elif response.POST.get("back"):
				return HttpResponseRedirect("/home")

		return render(response, "main/list.html",{"ls":ls})

	return render(response, "main/home.html",{})

def home(response):

	return render(response, "main/home.html", {})

def create(response):
	if response.method == "POST":
		if response.POST.get("newlist"):

			form = CreateNewList(response.POST)

			if form.is_valid():
				n = form.cleaned_data["name"]
				t = ToDoList(name=n)
				t.save()
				response.user.todolist.add(t)

				return HttpResponseRedirect("/%i" %t.id)

	else:
		form = CreateNewList()

	form = CreateNewList()
	return render(response, "main/create.html",{"form":form})


def delete(response):
	# all_objects = ToDoList.objects.all()
	all_objects = response.user.todolist.all()
	# if all_objects in response.user.todolist.all():


	if response.method == "POST":
		if response.POST.get("delete"):
			for obj in all_objects:
				if response.POST.get(str(obj.id)) == "clicked":
					obj.delete()
					return HttpResponseRedirect("/delete")
				else:
					pass

	return render(response, "main/delete.html",{"all_objects":all_objects})

	# return render(response, "main/delete.html",{})

def edit(response,id):
	ls = ToDoList.objects.get(id = id)

	if response.method == "POST":
		print(response.POST)
		if response.POST.get("delete"):
			for item in ls.item_set.all():
				if response.POST.get("c" + str(item.id)) == "clicked":
					item.delete()

		if response.POST.get("edit"):
			for item in ls.item_set.all():
				if response.POST.get("c" + str(item.id)) == "clicked":
					oldtext = response.POST.get(lis)

		if response.POST.get("back"):
			return HttpResponseRedirect("/home")

	return render(response, "main/edit.html",{"ls":ls})


	