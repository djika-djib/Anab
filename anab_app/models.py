from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify
# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # additional classes
    # School = models.CharField()

    # profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username

class Partenaire(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=250)
    text = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/')


    def __str__(self):
        return self.name

   

    
class Actu(models.Model):
    titre = models.CharField(max_length=250)
    text = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/')
    date = models.DateField()

    def __str__(self):
        return self.titre

class DemandeSimple(models.Model):

    options = [
            ('option1', 'Demande de Renouvellement de la bourse'),
            ('option2', 'Demande de Remboursement des frais de scolarites')
        ]
    Type_De_Demande = models.CharField(
        max_length=100,
        choices=options,
        default='Demande de Renouvellement de la bourse',
    )
    Nom = models.CharField(max_length=250)
    Prenom = models.CharField(max_length=250)
    Carte_D_etudiant = models.FileField(upload_to='documents/')
    Recu = models.FileField(upload_to='documents/')
    Releve_Notes = models.FileField(upload_to='documents/') 


    def __str__(self):
        fullName = self.Nom + ' '+ self.Prenom
        return fullName


# class Renouvellement(models.Model):
#     Nom = models.CharField(max_length=250)
#     Prenom = models.CharField(max_length=250)
#     Carte_etudiant = models.FileField(upload_to='documents/')
#     Recu = models.FileField(upload_to='documents/')
#     Releve_Notes = models.FileField(upload_to='documents/')
#     slug = models.CharField(max_length=250, null=True, blank=True)


#     def __str__(self):
#         fullName = self.Nom + ' '+ self.Prenom
#         return fullName

    # def save(self,*args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.name)
    #     return super().save(*args, **kwargs)
# Doit mettre une legende pour determiner l'annee de renouvellement