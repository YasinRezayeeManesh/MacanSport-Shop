from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Companies)
class CompaniesAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    pass


@admin.register(models.FrequentlyQuestions)
class FrequentlyQuestionsAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'job')


@admin.register(models.ManyInfo)
class ManyInfoAdmin(admin.ModelAdmin):
    pass
