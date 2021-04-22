from django.shortcuts import redirect, render
from django.http import HttpResponse,HttpResponseRedirect
from .models import ToDoList,Item
from .forms import CreateNewList
# Create your views here.


def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        print("1")
        if form.is_valid():
            print("2")
            n = form.cleaned_data["name"]
            print("3")
            t = ToDoList(n)
            print("4")
            t.save()
            print("5")
            print(t.id)
            u = ToDoList.objects.get(name=n).id
        return HttpResponseRedirect("/%i" %u)
    else:
        form = CreateNewList()
    return render(response,"main/create.html", {"form":form})

def index(response,id):
    list = ToDoList.objects.get(id=id)
    # item = list.item_set.get(id=id)
    if response.method == "POST":
        print("1")
        print(response.POST)
        print("2")
        # for item in list.item_set.all():
        #     print(item,item.id)
        # if response.POST.get("save"):
        print("3")
        for item in list.item_set.all():
            print("4")
            print("HERE!!!!! ======= {}".format(response.POST.get("c" + str(item.id))))
            if response.POST.get("c" + str(item.id)) == "checked":
                print(item.id, "working")
                item.complete = True
            else:
                item.complete =False
        item.save()
        # elif response.POST.get("newItem"):
        #     text = response.POST.get("new")
        #     if len(text) > 0:
        #         list.item_set.create(text=text, complete=False)
        #     else:
        #         print("invalid input")
             
    return render(response,"main/list.html", {"list" : list})

def home(response):
    return render(response,"main/home.html", {})

