from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage

from food.models import Company
from food.models import Category

module = "company"


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = [
            "logo",
            "name",
            "email",
            "phone",

            "category_id",
            "desconto",

            "mon","mon_open","mon_close",
            "tue","tue_open","tue_close",
            "wed","wed_open","wed_close",
            "thu","thu_open","thu_close",
            "fri","fri_open","fri_close",
            "sat","sat_open","sat_close",
            "sun","sun_open","sun_close",

            "localizacao",
            "lat","lng",

            "photo1",
            "photo2",
            "photo3",
            "photo4",
            "photo5",
        ]

def index(request, template_name="food/"+module+"/list.html"):
    if not request.user.is_authenticated:
        return redirect("/admin/login")
    company = Company.objects.all()
    data = {}
    data["object_list"] = company
    return render(request, template_name, data)

def store(request, template_name="food/"+module+"/form.html"):

    categories = Category.objects.all()
    if request.method == "GET":
        return render(request, template_name,{
            "categories":categories
        })

    request.POST._mutable = True
    data = validate(request)

    form = CompanyForm(data or None,request.FILES)
    if form.is_valid():
        form.save()
        return redirect(module+"_list")
    
    return render(request, template_name, {
        "form":form,
        "categories":categories
    })

def update(request, pk, template_name="food/"+module+"/form.html"):
    categories = Category.objects.all()

    company = get_object_or_404(Company, pk=pk)
    
    if request.method == "GET":
        return render(request, template_name, {
            "object":company,
            "categories":categories
        })

    request.POST._mutable = True
    data = validate(request)

    form = CompanyForm(data or None,request.FILES ,instance=company)
    if form.is_valid():
        form.save()
        return redirect(module+"_list")
    return render(request, template_name, {
        "form":form, 
        "object":company,
        "categories":categories
    })

def delete(request, pk, template_name="food/"+module+"/form.html"):
    company= get_object_or_404(Company, pk=pk)    
    company.delete()
    return redirect(module+"_list")


def validate(request):

    data = request.POST
    data['mon'] = True if data.get('mon') and data['mon'] == 'on' else False
    data['tue'] = True if data.get('tue') and data['tue'] == 'on' else False
    data['wed'] = True if data.get('wed') and data['wed'] == 'on' else False
    data['thu'] = True if data.get('thu') and data['thu'] == 'on' else False
    data['fri'] = True if data.get('fri') and data['fri'] == 'on' else False
    data['sat'] = True if data.get('sat') and data['sat'] == 'on' else False
    data['sun'] = True if data.get('sun') and data['sun'] == 'on' else False

    print(data)
    return data