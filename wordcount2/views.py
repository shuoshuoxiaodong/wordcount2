from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')


def count(request):
    text=request.GET['text']  #请求得到home.html中的text的值
    print(text)
    result={}  #定义一个字典
    for i in text:   #遍历text的值
        if i not in result:
            result[i]=1
        else:
            result[i]+=1
    print(result)
    result=sorted(result.items(),key=lambda x:x[1],reverse=True)   #按照词频由高到低排序
    return render(request,'count.html',{'count_result':result})#第2 部分是请求转到的网页（即跳转的网页）第3部分是传过去的模板变量