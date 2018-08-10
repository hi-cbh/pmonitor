from django.db import models

# 用例
class Case(models.Model):
    # kid = models.IntegerField()  # id
    times = models.TextField()  # time
    testcaseonbtnlogin = models.IntegerField()
    testcaselogin = models.IntegerField()
    testcasesendnoattach = models.IntegerField()
    testcasesendattach = models.IntegerField()
    testcasefwdsend = models.IntegerField()
    testcaseforward = models.IntegerField()
    testcasereply = models.IntegerField()
    testdownfile = models.IntegerField()
    testcasecheckaddresslist = models.IntegerField()
    testcaseselected = models.IntegerField()
    testcasepush = models.IntegerField()
    testcasecalendar = models.IntegerField()
    testcasediscover = models.IntegerField()
    testcasepersionmessages = models.IntegerField()
    testcaseskydrive = models.IntegerField()

    def __str__(self):
        return self.times


class Error(models.Model):
    # kid = models.IntegerField()  # id
    times = models.TextField()  # time
    testcaseonbtnlogin = models.IntegerField()
    testcaselogin = models.IntegerField()
    testcasesendnoattach = models.IntegerField()
    testcasesendattach = models.IntegerField()
    testcasefwdsend = models.IntegerField()
    testcaseforward = models.IntegerField()
    testcasereply = models.IntegerField()
    testdownfile = models.IntegerField()
    testcasecheckaddresslist = models.IntegerField()
    testcaseselected = models.IntegerField()
    testcasepush = models.IntegerField()
    testcasecalendar = models.IntegerField()
    testcasediscover = models.IntegerField()
    testcasepersionmessages = models.IntegerField()
    testcaseskydrive = models.IntegerField()

    def __str__(self):
        return self.times


class HourError(models.Model):
    # kid = models.IntegerField()  # id
    hour = models.IntegerField()
    times = models.TextField()  # time
    testcaseonbtnlogin = models.IntegerField()
    testcaselogin = models.IntegerField()
    testcasesendnoattach = models.IntegerField()
    testcasesendattach = models.IntegerField()
    testcasefwdsend = models.IntegerField()
    testcaseforward = models.IntegerField()
    testcasereply = models.IntegerField()
    testdownfile = models.IntegerField()
    testcasecheckaddresslist = models.IntegerField()
    testcaseselected = models.IntegerField()
    testcasepush = models.IntegerField()
    testcasecalendar = models.IntegerField()
    testcasediscover = models.IntegerField()
    testcasepersionmessages = models.IntegerField()
    testcaseskydrive = models.IntegerField()

    def __str__(self):
        return self.hour