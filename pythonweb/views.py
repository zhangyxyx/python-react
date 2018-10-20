from django.shortcuts import render
#coding=utf-8
# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

import xlrd
from collections import OrderedDict
import json
import codecs
import xlwt
from django.shortcuts import render
from django.http import JsonResponse
from pythonweb.models import Mobile
from pythonweb.models import Essay
from pythonweb.models import Question


# Create your views here.
def index(request):
    str = Mobile.objects.all()
    return render(request, 'index.html', {'str': str})

def ajax_list(request):
    a={'key': '123'}
    return JsonResponse(a)

def essay(request):
    essayData=Essay.objects.all()
    return render(request, 'essay.html', {'essayData':essayData})


def question(request):
    questionData=Question.objects.all()
    context = '''{
        "success": '1',
        "data": [
            {"id": "1", "title": "关注干货：搭建自己的Git服务器",
             "con": "前言：Git是一款非常好用的版本管理器，对于开源项目，我们可以托管到GitHub，但是闭源项目GitHub的收费非常昂贵。实验室有一部分工作是需", "user": "OneXzgj",
             "common": 20, "like": 10,
             "pic": "//upload-images.jianshu.io/upload_images/10612886-244d0f50b69c2185.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/300/h/240"},
            {"id": "2", "title": "李开复告诉你：算法的力量",
             "con": "算法是计算机科学领域最重要的基石之一，但却受到了国内一些程序员的冷落。许多同学看到一些公司在招聘时要求的编程语言五花八门就产生了一种误解，认为学...", "user": "OneXzgj",
             "common": 20, "like": 10,
             "pic": "//upload.jianshu.io/collections/images/21/20120316041115481.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/64/h/64"},
            {"id": "3", "title": "外包程序员被当猴耍，1000做个百度，明天要上线！",
             "con": "拿最低的工资，干最苦的活，这就是外包程序员的日常。外包程序员，是指帮其他公司做开发的一群人，他们总要面对一些“外行”人的指挥，看着天马行空的需求...", "user": "OneXzgj",
             "common": 20, "like": 10,
             "pic": "//upload.jianshu.io/collections/images/21/20120316041115481.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/64/h/64"},
            {"id": "4", "title": "30个极大提高开发效率的Visual Studio Code插件",
             "con": "译者按： 看完这篇文章，我打算从 Sublime Text 转到 Visual Studio Code 了！ 原文: Immensely upg...", "user": "OneXzgj",
             "common": 20, "like": 10,
             "pic": "//upload.jianshu.io/collections/images/21/20120316041115481.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/64/h/64"},
            {"id": "5", "title": "Spring Boot（5）一个极简且完整的后台框架",
             "con": "一个完整的极简后台框架，方便做小项目的时候可以快速开发。 这里面多贴图片和代码，做个参考吧，代码可以下载下来自己看看，里面这套后台模板不错，喜欢...", "user": "OneXzgj",
             "common": 20, "like": 10,
             "pic": "//upload.jianshu.io/collections/images/21/20120316041115481.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/64/h/64"},
            {"id": "6", "title": "如果这样来理解HTTPS，一篇就够了！",
             "con": "1、前言 可能有初学者会问，即时通讯应用的通信安全，不就是对Socket长连接进行SSL/TLS加密这些知识吗，干吗要理解HTTPS协议呢。 这...", "user": "OneXzgj",
             "common": 20, "like": 10,
             "pic": "//upload.jianshu.io/collections/images/21/20120316041115481.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/64/h/64"},
            {"id": "7", "title": "学会了Python出门不担心没有WiFi了Python几行代码就可以做到！进来就学会",
             "con": "是不是还在为WiFi密码发愁，甚至有时候还忘掉自己家的WiFi密码，没关系，今天我给大家带来几个破解WiFi密码的案例！我先说明下这个东西一点都...", "user": "OneXzgj",
             "common": 20, "like": 10,
             "pic": "//upload.jianshu.io/collections/images/21/20120316041115481.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/64/h/64"},
            {"id": "8", "title": "自控力差？！推荐这款神器保证你安心工作学习",
             "con": "酷友们，大家好。 每天工作或学习，忙忙碌碌的一天，却又感觉什么事都没有做，工作学习都没有完成。那是什么原因造成的呢？很大一部分是浏览一些娱乐等与...", "user": "OneXzgj",
             "common": 20, "like": 10,
             "pic": "//upload.jianshu.io/collections/images/21/20120316041115481.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/64/h/64"},
            {"id": "9", "title": "TODO 最适合练习主流框架的应用",
             "con": "1、应用介绍: 使用MVP+Dagger2+Retrofit+Rxjava2+RxLifecycle+ARouter框架构建一般使用该框架的应用", "user": "OneXzgj",
             "common": 20, "like": 10,
             "pic": "//upload.jianshu.io/collections/images/21/20120316041115481.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/64/h/64"}
        ]
    }'''

    return HttpResponse(context)
    #def get(self,requset):
        # questionData=Question.objects.all()
        # context = {'questionData': questionData}
        # print(questionData)

        #render(request,'question.html',context)
def react(request):
    # SERVER_ADDR = settings.SERVER_ADDR
    print(1)
    return render(request, 'react/index.html')

def execl2(request):
    wb = xlrd.open_workbook('static/files/1.xlsx')
    convert_list = []
    sh = wb.sheet_by_index(0)
    title = sh.row_values(0)
    for rownum in range(1, sh.nrows):
        rowvalue = sh.row_values(rownum)
        single = OrderedDict()
        for colnum in range(0, len(rowvalue)):
            print(title[colnum], rowvalue[colnum])
            single[title[colnum]] = rowvalue[colnum]
        convert_list.append(single)

    j = json.dumps(convert_list)

    with codecs.open('static/json/10.json',"w","utf-8") as f:
        f.write(j)

    return HttpResponse(1)

def execl(request):
    limit = 50
    readbook = "static/execl.xlsx"  # 原始文件路径
    savebook = "e:\\execlfiles"  # 要保存的目录
    data = xlrd.open_workbook(readbook)
    # 获取sheet
    table = data.sheets()[0]  # 获取第一个sheet的所有数据

    # 行数
    nrows = table.nrows
    # 列数
    ncols = table.ncols

    sheets = nrows / limit  # 总共需要多少excel

    if not sheets.is_integer():  # 如果不是整除则需要+1
        sheets = sheets + 1

    title_row = table.row_values(0)  # 获取首行的标题
    #
    for i in range(0, int(sheets)):
        workbook = xlwt.Workbook(encoding='ascii')
        worksheet = workbook.add_sheet(sheetname="0")  # 设置sheet名称
        for col in range(0, ncols):  # 写首行的标题
            worksheet.write(0, col, title_row[col])
        for row in range(1, limit + 1):  # 每次循环limit行
            newRow = row + limit * i
            if newRow < nrows:
                row_content = table.row_values(newRow)
                for col in range(0, ncols):
                    worksheet.write(row, col, row_content[col])
        workbook.save(savebook + "\\" + str(i) + ".xlsx")

    return HttpResponse(1)
