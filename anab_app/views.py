from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from anab_app.forms import UserForm, DemandeSimpleForm
from anab_app.models import Partenaire, Service, Actu

from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    partenaires = Partenaire.objects.all()
    services = Service.objects.all()
    actus = Actu.objects.all()
    return render(request, 'index.html', {'partenaires': partenaires,
                                          'services': services, 
                                          'actus': actus})

def portfolio(request): 
    return render(request, 'portfolio-details.html')

def services(request): 
    services = Service.objects.all()
    demandes_form = DemandeSimpleForm()
    
    if request.method == 'POST': 
        demandes_form = DemandeSimpleForm(request.POST, request.FILES)

        if demandes_form.is_valid():
            demandes_form.save()
            return HttpResponse("Merci d'avoir soumis cet formulaire.")
        else:
            return HttpResponse("Erreur de soumission.")
            
    return render(request, 'services.html', {'services': services,
                                             'demandes_form': demandes_form,})

# def renouvellement(request, slug):
    renouvellement = Renouvellement.objects.get(slug=slug)

    renouvellement_form = RenouvellemntForm()

    if request.method == 'POST':
        renouvellement_form = RenouvellemntForm(request.POST, request.FILES)

        if renouvellement_form.is_valid():
            renouvellement_form.save()
            return HttpResponse("Merci d'avoir soumis cet formulaire.")
        else:
            return HttpResponse("Erreur de soumission.")

    return render(request, 'renouvellement.html', {'renouvellement_form': renouvellement_form,
                                                   'renouvellement':renouvellement})


def contact(request): 
    return render(request, 'contact.html')


def registration(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        # profile_form = UserProfileInfoForm(data=request.POST)
# and profile_form.is_valid()
        if user_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            # profile = profile_form.save(commit=False)
            # profile.user = user

            # if 'profile_pic' in request.FILES:
            #     profile.profile_pic = request.FILES['profile_pic']

            # profile.save()

            registered = True
        else:
            # , profile_form.errors
            print(user_form.errors) 
    else:
        user_form = UserForm()
        # profile_form = UserProfileInfoForm()
    
    return render(request, 'registration.html',
                           {'user_form':user_form,
                            # 'profile_form':profile_form,
                            'registered':registered})
    
 
def special(request):
    HttpResponse("You are logged in, Nice!!!")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

    
def user_login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('services'))
            else: 
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else: 
            print("Someone tried to login and failed!!!")
            print("Username: {} and password: {}".format(username,password))
            return HttpResponse("INVALID Login details supplied!")
    else:
        return render(request, 'login.html', {})
