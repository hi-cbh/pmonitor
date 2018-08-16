from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader
from pyecharts import Bar3D
from sign.models import HourError
REMOTE_HOST = "https://pyecharts.github.io/assets/js"


def index(request):
    # template = loader.get_template('myfirstvis/pyecharts.html')
    template = loader.get_template('myfirstvis/pyecharts.html')
    l3d = line3d()
    context = dict(
        myechart=l3d.render_embed(),
        host=REMOTE_HOST,
        script_list=l3d.get_js_dependencies()
    )
    return HttpResponse(template.render(context, request))


def getdatal(case_list):
    data_l = []
    for i in range(12):
        for x in case_list[i].testcaseonbtnlogin:
            data_l.append(x)


def line3d():

    case_list = HourError.objects.all()

    new_case={}

    new_case["testcaseonbtnlogin"] = [case_list[x].testcaseonbtnlogin for x in range(24) ]
    new_case["testcaselogin"] = [case_list[x].testcaselogin for x in range(24) ]
    new_case["testcasesendnoattach"] = [case_list[x].testcasesendnoattach for x in range(24) ]
    new_case["testcasesendattach"] = [case_list[x].testcasesendattach for x in range(24) ]
    new_case["testcasefwdsend"] = [case_list[x].testcasefwdsend for x in range(24) ]
    new_case["testcaseforward"] = [case_list[x].testcaseforward for x in range(24) ]
    new_case["testcasereply"] = [case_list[x].testcasereply for x in range(24) ]
    new_case["testdownfile"] = [case_list[x].testdownfile for x in range(24) ]
    new_case["testcasecheckaddresslist"] = [case_list[x].testcasecheckaddresslist for x in range(24) ]
    new_case["testcaseselected"] = [case_list[x].testcaseselected for x in range(24) ]
    new_case["testcasepush"] = [case_list[x].testcasepush for x in range(24) ]
    new_case["testcasecalendar"] = [case_list[x].testcasecalendar for x in range(24) ]
    new_case["testcasediscover"] = [case_list[x].testcasediscover for x in range(24) ]
    new_case["testcasepersionmessages"] = [case_list[x].testcasepersionmessages for x in range(24) ]
    new_case["testcaseskydrive"] = [case_list[x].testcaseskydrive for x in range(24) ]


    # print("testdata--------")
    # print(new_case)

    _data = []
    num = 0
    for k in new_case.keys():
        for y in range(24):
            if y == 23:
                _data.append([num, 0,new_case[k][y]])
            else:
                _data.append([num, y+1,new_case[k][y]])
        num = num + 1


    case={'testcaseonbtnlogin': "一键登录", 'testcaselogin': "账号登录", 'testcasesendnoattach': "无附发送", 'testcasesendattach': "有附发送", 'testcasefwdsend': "云端转发", 'testcaseforward': "SMTP转发", 'testcasereply': "回复", 'testdownfile': "下载附件", 'testcasecheckaddresslist': "联系人同步", 'testcaseselected': "139精选", 'testcasepush': "推送", 'testcasecalendar': "日历", 'testcasediscover': "发现主页", 'testcasepersionmessages': "个人资料", 'testcaseskydrive': "彩云网盘"}
    casename = [case[k]  for k in new_case.keys()]
    casetime = [str(x) for x in range(0,24)]
    # print(_data)

    # print("testdata--------")



    bar3d = Bar3D("错误分布图", width=1200, height=700)
    x_axis = casetime

    y_axis = casename


    range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
                   '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
    bar3d.add("错误次数", x_axis, y_axis, [[d[1], d[0], d[2]] for d in _data],
              is_visualmap=True, visual_range=[0, 10],
              visual_range_color=range_color, grid3d_width=200,
              grid3d_depth=80, grid3d_shading='lambert' ,yaxis3d_interval= 0, xaxis3d_interval=0)
    return bar3d