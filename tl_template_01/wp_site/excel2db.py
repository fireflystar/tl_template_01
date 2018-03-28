from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import xlrd#处理excel
import os#拼凑excel文件的地址
from . import models


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
        list_of_row = table.row_values(row)#m每一行的全部字段，放入一个列表中
        # print(list_of_row)
        rows.append(list_of_row)


        #为想数据库插入内容准备数据
        post_content = list_of_row[4]   #某一行的第4列
        post_title = list_of_row[5]     # 某一行的第5列
        
        #发送到前端模板去看看都取得了什么数据
        l = [post_content,post_content]
        db_lists.append(l)

        if models.WpPosts.objects.filter(post_content=post_content,post_title=post_title):pass
        else:
            models.WpPosts.objects.create(post_content=post_content,post_title=post_title)
    return (rows, db_lists)



def transfer(request):
    if request.method == "GET":


        fileName = os.path.join(\
                os.path.dirname(os.path.realpath(__file__)), '3-wp_posts.xlsx')
        (rows, db_lists)= excel_table_byIndex(fileName=fileName, byIndex=0)#注意这里是要修改的地方
        return render(request,"insert2db.html", {"rows":rows,"db_lists":db_lists})