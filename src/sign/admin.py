from django.contrib import admin
from sign.models import Case

class CaseAdmin(admin.ModelAdmin):
    list_display = ['id','times','testcaseonbtnlogin','testcaselogin','testcasesendnoattach','testcasesendattach','testcasefwdsend','testcaseforward','testcasereply','testdownfile','testcasecheckaddresslist','testcaseselected','testcasepush','testcasecalendar','testcasediscover','testcasepersionmessages','testcaseskydrive']

admin.site.register(Case)

