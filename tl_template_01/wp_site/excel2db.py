from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import xlrd#处理excel
import os#拼凑excel文件的地址
from . import models

"""
excel 表格 3-wp_posts.xlsx中，只有下面2个字段里有值
准备搬运这2个字段的内容到数据中，并把搬运的内容显示到网页中
post_title
post_content


需要些一个template html  ，准备渲染，并返回给用户  
    创建 insert2db.html  
需要修改urls.py的内容，新的文件中的处理函数要和 网址建立关联

    from wp_site import excel2db
    urlpatterns += [
        path('excel2db', excel2db.transfer),

    ]

"""
def excel_table_byIndex(fileName, byIndex=0):
    # 可以先发送到前端看看，并不直接往数据库中插入，当结果调整好了之后再插入到数据库
    data_excel = ''
    try:
        data_excel = xlrd.open_workbook(fileName)
    except Exception as e:
        print('open_workbook函数打印的异常信息' + str(e))
    else:
        pass
    finally:
        pass
        
    table = data_excel.sheets()[byIndex]    #默认为第一个sheet
    # print(table.name)# exel表格中指定sheet的具体名字

    nrows = table.nrows#行数

    rows = list()   #里面放很多个行
    db_lists = list()
    for row in range(1, nrows):#这里设置从sheet的第多少行开始获取数据
        list_of_row = table.row_values(row)#m每一行的内容，放入一个列表中
        # print(list_of_row)
        rows.append(list_of_row)


        #为想数据库插入内容准备数据
        post_content = list_of_row[4]   #某一行的第4列
        post_title = list_of_row[5]     # 某一行的第5列
        
        #发送到前端模板去看看都取得了什么数据
        l = [post_content,post_content]
        db_lists.append(l)

    return (rows, db_lists)



def transfer(request):
    if request.method == "GET":
        # os.path.dirname(os.path.realpath(__file__))#当前文件的所在的文件夹
        # os.path.realpath(__file__)#当前文件的真实路径

        fileName = os.path.join(\
                os.path.dirname(os.path.realpath(__file__)), '3-wp_posts.xlsx')
        (rows, db_lists)= excel_table_byIndex(fileName=fileName, byIndex=0)#注意这里是要修改的地方
        return render(request,"insert2db.html", {"rows":rows,"db_lists":db_lists})
