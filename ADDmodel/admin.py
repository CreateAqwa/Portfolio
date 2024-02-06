from django.contrib import admin
# Register your models here.
from ADDmodel.models import monelN
from ADDmodel.models import project
from ADDmodel.models import skill



# class anynam(admin.ModelAdmin):
# 	list_display=("LanguageName","WhatSpecial","Disc")
# admin.site.register(skill,anynam)


class ProjectAdmin(admin.ModelAdmin):
	list_display=("ProjectName","LanguageUse","Year")
admin.site.register(project,ProjectAdmin)


class monelNAdmin(admin.ModelAdmin):
	list_display=("name","Photo","subTitle")
admin.site.register(monelN,monelNAdmin)


class skillAdmin(admin.ModelAdmin):
	list_display=("LanguageName","WhatSpecial","Disc")
admin.site.register(skill,skillAdmin)