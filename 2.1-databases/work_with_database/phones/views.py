from django.shortcuts import get_object_or_404, render, redirect

from phones.models import Phone


def index(request):
    return redirect("catalog")


def show_catalog(request):
    template = "catalog.html"
    context = {}
    return render(request, template, context)


def show_product(request, slug):
    template = "product.html"
    context = {}
    return render(request, template, context)


def phone_catalog(request):
    # Получаем порядок сортировки из GET-параметров
    sort_by = request.GET.get("sort", "name")  # По умолчанию сортируем по имени
    if sort_by == "price_asc":
        phones = Phone.objects.all().order_by("price")
    elif sort_by == "price_desc":
        phones = Phone.objects.all().order_by("-price")
    else:
        phones = Phone.objects.all().order_by("name")

    context = {"phones": phones}
    return render(request, "catalog.html", context)


def phone_detail(request, slug):
    phone = get_object_or_404(Phone, slug=slug)
    context = {"phone": phone}
    return render(request, "phone_detail.html", context)
