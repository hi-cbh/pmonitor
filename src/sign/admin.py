from django.contrib import admin
from sign.models import Case
from sign.models import Error

class CaseAdmin(admin.ModelAdmin):
    list_display = ['id','times','testcaseonbtnlogin','testcaselogin','testcasesendnoattach','testcasesendattach','testcasefwdsend','testcaseforward','testcasereply','testdownfile','testcasecheckaddresslist','testcaseselected','testcasepush','testcasecalendar','testcasediscover','testcasepersionmessages','testcaseskydrive']

class ErrorAdmin(admin.ModelAdmin):
    list_display = ['id','times','testcaseonbtnlogin','testcaselogin','testcasesendnoattach','testcasesendattach','testcasefwdsend','testcaseforward','testcasereply','testdownfile','testcasecheckaddresslist','testcaseselected','testcasepush','testcasecalendar','testcasediscover','testcasepersionmessages','testcaseskydrive']


admin.site.register(Case)
admin.site.register(Error)

