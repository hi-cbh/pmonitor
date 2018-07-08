# coding=utf8


from pyecharts import Bar

from sign.models import Case
from sign.sql import DB


class ChartFactory:
    def __init__(self):
        self._func = {}
        self._charts = {}

    def collect(self, name):
        def _inject(func):
            self._func[name] = func
            return func

        return _inject

    def create(self, name):
        if name in self._func:
            chart = self._func[name]()
            return chart
        else:
            raise ValueError('No Chart builder for {}'.format(name))


FACTORY = ChartFactory()


@FACTORY.collect('bar')
def create_simple_bar():
    print("------------------------")
    case_list = Case.objects.all()

    new_case={}

    new_case["times"] = case_list[0].times
    new_case["testcaseonbtnlogin"] = case_list[0].testcaseonbtnlogin
    new_case["testcaselogin"] = case_list[0].testcaselogin
    new_case["testcasesendnoattach"] = case_list[0].testcasesendnoattach
    new_case["testcasefwdsend"] = case_list[0].testcasefwdsend
    new_case["testcaseforward"] = case_list[0].testcaseforward
    new_case["testcasereply"] = case_list[0].testcasereply
    new_case["testdownfile"] = case_list[0].testdownfile
    new_case["testcasecheckaddresslist"] = case_list[0].testcasecheckaddresslist
    new_case["testcaseselected"] = case_list[0].testcaseselected
    new_case["testcasepush"] = case_list[0].testcasepush
    new_case["testcasecalendar"] = case_list[0].testcasecalendar
    new_case["testcasediscover"] = case_list[0].testcasediscover
    new_case["testcasepersionmessages"] = case_list[0].testcasepersionmessages
    new_case["testcaseskydrive"] = case_list[0].testcaseskydrive


    # for obj in case_list:
    #     print( obj.times)
    print(new_case)

    print("------------------------")

    case={'testcaseonbtnlogin': "一键登录", 'testcaselogin': "账号登录", 'testcasesendnoattach': "无附发送", 'testcasesendattach': "有附发送", 'testcasefwdsend': "云端转发", 'testcaseforward': "SMTP转发", 'testcasereply': "回复", 'testdownfile': "下载附件", 'testcasecheckaddresslist': "联系人同步", 'testcaseselected': "139精选", 'testcasepush': "推送", 'testcasecalendar': "日历", 'testcasediscover': "发现主页", 'testcasepersionmessages': "个人资料", 'testcaseskydrive': "彩云网盘"}
    casename=[]
    db = DB()




    # result=db.show_data("test_data")
    # # print(result[0])
    # l=[]
    # for k,v in result[0].items():
    #     # print(v)
    #     if k in case.keys():
    #         casename.append(case[k])
    #     l.append(v)

    # print(result[0])
    l=[]
    for k,v in new_case.items():
        # print(v)
        if k in case.keys():
            casename.append(case[k])
        l.append(v)

    print(l)
    print(casename)
    # print(case.keys())
    db.close()





    # X_AXIS = ["一键登录", "账号登录", "无附发送", "有附发送", "云端转发", "SMTP转发","回复","139精选","发现主页","彩云网盘","个人资料","联系人同步","日历","推送","下载附件"]
    bar = Bar("记录连续错误测试", "数据更新: "+l[0])
    bar.add("错误次数",casename , l[1:],bar_category_gap="20%",xaxis_interval=0)

    bar.renderer = 'svg'
    return bar
