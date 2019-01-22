# coding=utf-8
from django.forms.models import model_to_dict
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.core import serializers
from app01 import models
import datetime
import hashlib


# Create your views here.
def home(request):
    """
    首页
    :param request:
    :return:
    """
    if request.method == 'GET':
        emp_result = models.Emp.objects.all()
        return render(request, 'home.html', {'emp_result': emp_result})


def add(request, nid):
    """
    添加
    :param nid:
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, 'edit.html', {'url': '/app01/add-0/', 'deptno': -1})
    elif request.method == 'POST' and nid == '0':
        empno = request.POST.get('empno', None)
        ename = request.POST.get('ename', None)
        job = request.POST.get('job', None)
        mgr = request.POST.get('mgr', None)
        hiredate = request.POST.get('hiredate', None)
        sal = request.POST.get('sal', None)
        comm = request.POST.get('comm', None)
        deptno = request.POST.get('deptno', None)
        data = {'empno': empno, 'ename': ename, 'job': job, 'mgr': mgr,
                'hiredate': datetime.datetime.strptime(hiredate, '%Y-%m-%d %H:%M:%S'), 'sal': sal, 'comm': comm,
                'deptno': models.Dept.objects.get(deptno=deptno)}
        # 把数据存入数据库
        models.Emp.objects.create(**data)
    elif request.method == 'POST' and nid == '1':
        empno = request.POST.get('empno', None)
        ename = request.POST.get('ename', None)
        job = request.POST.get('job', None)
        mgr = request.POST.get('mgr', None)
        hiredate = request.POST.get('hiredate', None)
        sal = request.POST.get('sal', None)
        comm = request.POST.get('comm', None)
        deptno = request.POST.get('deptno', None)
        data = {'ename': ename, 'job': job, 'mgr': mgr,
                'hiredate': datetime.datetime.strptime(hiredate, '%Y-%m-%d %H:%M:%S'), 'sal': sal, 'comm': comm,
                'deptno': models.Dept.objects.get(deptno=deptno)}
        # 把数据存入数据库
        models.Emp.objects.filter(empno=empno).update(**data)
    return redirect('/app01/home/')


def edit(request, nid):
    emp_data = models.Emp.objects.filter(empno=nid)
    row = {}
    for i in emp_data:
        row = i
    return render(request, 'edit.html',
                  {'data': row, 'url': '/app01/add-1/', 'deptno': row.deptno.deptno, 'readonly': 'readonly="readonly"'})


def dele(request, nid):
    models.Emp.objects.filter(empno=nid).delete()
    return redirect('/app01/home/')


def emp_ajax(request):
    dept_result = models.Dept.objects.all()
    data = serializers.serialize("json", dept_result, ensure_ascii=False)
    return HttpResponse(data)


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        u = request.POST.get('user[email]')
        p = request.POST.get('user[password]')
        power = request.POST.get('user[power]')
        user = models.User.objects.filter(uid=u)
        row = {}
        for i in user:
            row = i
        if row.pwd == hashlib.md5(p.encode('utf-8')).hexdigest():
            return redirect('/app01/home/')
        else:
            return render(request, 'login.html')


def adddb(request):
    """
    添加默认数据
    :param request:
    :return:
    """
    deptdb = (
        {'deptno': 1, 'dname': '会计', 'loc': '纽约州'},
        {'deptno': 2, 'dname': '研究', 'loc': '达拉斯'},
        {'deptno': 3, 'dname': '销售', 'loc': '芝加哥'},
        {'deptno': 4, 'dname': '业务', 'loc': '波士顿'}
    )
    for row in deptdb:
        try:
            model_to_dict(models.Dept.objects.filter(deptno=row['deptno']).first())['deptno']
        except AttributeError:
            models.Dept.objects.create(**row)
    empdb = (
        {'empno': 7369, 'ename': '史密斯', 'job': '文书 ', 'mgr': 7902,
         'hiredate': datetime.datetime.strptime('1980-12-17 12:00:00', '%Y-%m-%d %H:%M:%S'), 'sal': 800,
         'comm': 0, 'deptno': models.Dept.objects.get(deptno=2)},
        {'empno': 7499, 'ename': '爱伦	', 'job': '业务员', 'mgr': 7698,
         'hiredate': datetime.datetime.strptime('1981-02-20 12:00:00', '%Y-%m-%d %H:%M:%S'),
         'sal': 1600, 'comm': 300, 'deptno': models.Dept.objects.get(deptno=3)},
        {'empno': 7521, 'ename': '监护人', 'job': '业务员', 'mgr': 7698,
         'hiredate': datetime.datetime.strptime('1981-02-22 12:00:00', '%Y-%m-%d %H:%M:%S'), 'sal': 1250,
         'comm': 500, 'deptno': models.Dept.objects.get(deptno=3)},
        {'empno': 7566, 'ename': '琼斯	', 'job': '经营者', 'mgr': 7839,
         'hiredate': datetime.datetime.strptime('1981-04-02 12:00:00', '%Y-%m-%d %H:%M:%S'),
         'sal': 2975, 'comm': 0, 'deptno': models.Dept.objects.get(deptno=2)},
        {'empno': 7654, 'ename': '马丁	', 'job': '业务员', 'mgr': 7698,
         'hiredate': datetime.datetime.strptime('1981-09-28 12:00:00', '%Y-%m-%d %H:%M:%S'), 'sal': 1250,
         'comm': 1400, 'deptno': models.Dept.objects.get(deptno=3)},
        {'empno': 7698, 'ename': '布莱克', 'job': '经纪人', 'mgr': 7839,
         'hiredate': datetime.datetime.strptime('1981-05-01 12:00:00', '%Y-%m-%d %H:%M:%S'), 'sal': 2850,
         'comm': 0, 'deptno': models.Dept.objects.get(deptno=3)},
        {'empno': 7782, 'ename': '克拉克', 'job': '经纪人', 'mgr': 7839,
         'hiredate': datetime.datetime.strptime('1981-06-09 12:00:00', '%Y-%m-%d %H:%M:%S'), 'sal': 2450,
         'comm': 0, 'deptno': models.Dept.objects.get(deptno=1)},
        {'empno': 7788, 'ename': 'tom', 'job': '分析者', 'mgr': 7566,
         'hiredate': datetime.datetime.strptime('1987-04-19 12:00:00', '%Y-%m-%d %H:%M:%S'), 'sal': 3000,
         'comm': 0, 'deptno': models.Dept.objects.get(deptno=2)},
        {'empno': 7839, 'ename': '国王	', 'job': '总经理', 'mgr': 0,
         'hiredate': datetime.datetime.strptime('1981-11-17 12:00:00', '%Y-%m-%d %H:%M:%S'), 'sal': 5000,
         'comm': 0, 'deptno': models.Dept.objects.get(deptno=1)},
        {'empno': 7844, 'ename': '特纳	', 'job': '业务员', 'mgr': 7698,
         'hiredate': datetime.datetime.strptime('1981-09-08 12:00:00', '%Y-%m-%d %H:%M:%S'), 'sal': 1500,
         'comm': 0, 'deptno': models.Dept.objects.get(deptno=3)},
        {'empno': 7876, 'ename': '亚当斯', 'job': '职员', 'mgr': 7788,
         'hiredate': datetime.datetime.strptime('1987-05-23 12:00:00', '%Y-%m-%d %H:%M:%S'), 'sal': 1100,
         'comm': 0, 'deptno': models.Dept.objects.get(deptno=2)},
        {'empno': 7900, 'ename': '詹姆斯', 'job': '职员', 'mgr': 7698,
         'hiredate': datetime.datetime.strptime('1981-12-03 12:00:00', '%Y-%m-%d %H:%M:%S'), 'sal': 950,
         'comm': 0, 'deptno': models.Dept.objects.get(deptno=3)},
        {'empno': 7902, 'ename': '福特	', 'job': '分析者', 'mgr': 7566,
         'hiredate': datetime.datetime.strptime('1981-12-03 12:00:00', '%Y-%m-%d %H:%M:%S'),
         'sal': 3000, 'comm': 0, 'deptno': models.Dept.objects.get(deptno=2)},
        {'empno': 7934, 'ename': '磨坊主', 'job': '职员', 'mgr': 7782,
         'hiredate': datetime.datetime.strptime('1982-01-23 12:00:00', '%Y-%m-%d %H:%M:%S'), 'sal': 1300,
         'comm': 0, 'deptno': models.Dept.objects.get(deptno=1)}
    )
    for row in empdb:
        try:
            model_to_dict(models.Emp.objects.filter(empno=row['empno']).first())['empno']
        except AttributeError:
            models.Emp.objects.create(**row)
    return HttpResponse('add')
