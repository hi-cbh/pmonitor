# coding=utf8


from pyecharts import Bar
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
    case={'testcaseonbtnlogin': "一键登录", 'testcaselogin': "账号登录", 'testcasesendnoattach': "无附发送", 'testcasesendattach': "有附发送", 'testcasefwdsend': "云端转发", 'testcaseforward': "SMTP转发", 'testcasereply': "回复", 'testdownfile': "下载附件", 'testcasecheckaddresslist': "联系人同步", 'testcaseselected': "139精选", 'testcasepush': "推送", 'testcasecalendar': "日历", 'testcasediscover': "发现主页", 'testcasepersionmessages': "个人资料", 'testcaseskydrive': "彩云网盘"}
    casename=[]
    db = DB()
    result=db.show_data("test_data")
    # print(result[0])
    l=[]
    for k,v in result[0].items():
        # print(v)
        if k in case.keys():
            casename.append(case[k])
        l.append(v)

    # print(l[2:])
    # print(casename)
    # print(case.keys())
    db.close()





    # X_AXIS = ["一键登录", "账号登录", "无附发送", "有附发送", "云端转发", "SMTP转发","回复","139精选","发现主页","彩云网盘","个人资料","联系人同步","日历","推送","下载附件"]
    bar = Bar("记录连续错误测试", "这里更新时间戳")
    bar.add("错误次数",casename , l[2:],bar_category_gap="20%",xaxis_interval=0)

    bar.renderer = 'svg'
    return bar
