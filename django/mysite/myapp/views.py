from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
import json

from .models import BlogUser, User, HotBoard, BlogUserAll


# # Create your views here.
# @require_http_methods(["GET"])
# def add_person(request):
#     response = {}
#     try:
#         person = Person(
#             person_name=request.GET.get('person_name'),
#             deposit=request.GET.get('deposit')
#         )
#         person.save()
#         response['msg'] = 'success'
#         response['error_num'] = 0
#     except Exception as e:
#         response['msg'] = str(e)
#         response['error_num'] = 1
#     return JsonResponse(response)
#
#
# # 查询登录信息
# @require_http_methods(["GET"])
# def show_user(request):
#     response = {}
#     try:
#         users = User.objects.filter(user_username=request.GET.get('user_username'))
#         response['list'] = json.loads(serializers.serialize("json", users))
#         response['msg'] = 'success'
#         response['error_num'] = 0
#     except Exception as e:
#         response['msg'] = str(e)
#         response['error_num'] = 1
#     return JsonResponse(response)


# 获取商品信息
@require_http_methods(["GET"])
def show_BlogUser(request):
    response = {}
    try:
        bloguser = BlogUser.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", bloguser))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def add_user(request):
    response = {}
    try:
        user = User(
            User_name=request.GET.get('User_name'),
            User_passwd=request.GET.get('User_passwd'),
        )
        user.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def add_bloguserall(request):
    response = {}
    try:
        user = BlogUserAll(
            name=request.GET.get('name'),
        )
        user.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def show_hotboard(request):
    response = {}
    try:
        hotboard = HotBoard.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", hotboard))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

# # 获取订单信息
# @require_http_methods(["GET"])
# def show_paper(request):
#     response = {}
#     try:
#         paper = Paper.objects.filter()
#         response['list'] = json.loads(serializers.serialize("json", paper))
#         response['msg'] = 'success'
#         response['error_num'] = 0
#     except Exception as e:
#         response['msg'] = str(e)
#         response['error_num'] = 1
#     return JsonResponse(response)
#
#
# # 用户注册
# @require_http_methods(["GET"])
# def register(request):
#     response = {}
#     try:
#         user = User(
#             user_name=request.GET.get('user_name'),
#             user_username=request.GET.get('user_username'),
#             user_password=request.GET.get('user_password')
#         )
#         user.save()
#         response['msg'] = 'success'
#         response['error_num'] = 0
#     except Exception as e:
#         response['msg'] = str(e)
#         response['error_num'] = 1
#     return JsonResponse(response)
#
#
# # 创建商品
# def create_product(request):
#     response = {}
#     try:
#         product = Product(
#             product_name=request.GET.get('product_name'),
#             product_brand=request.GET.get('product_brand'),
#             product_img=request.GET.get('product_img'),
#             detail_img=request.GET.get('detail_img'),
#             product_sales=request.GET.get('product_sales'),
#             product_cost=request.GET.get('product_cost'),
#             product_color=request.GET.get('product_color'),
#             product_state=request.GET.get('product_state'),
#         )
#         product.save()
#         response['msg'] = 'success'
#         response['error_num'] = 0
#     except Exception as e:
#         response['msg'] = str(e)
#         response['error_num'] = 1
#     return JsonResponse(response)
#
#
# # 创建订单
# def create_paper(request):
#     response = {}
#     try:
#         paper = Paper(
#             paper_state=request.GET.get('paper_state'),
#             paper_time=request.GET.get('paper_time'),
#             user_id=request.GET.get('user_id'),
#             producer_id=request.GET.get('producer_id'),
#             produce_id=request.GET.get('produce_id'),
#         )
#         paper.save()
#         response['msg'] = 'success'
#         response['error_num'] = 0
#     except Exception as e:
#         response['msg'] = str(e)
#         response['error_num'] = 1
#     return JsonResponse(response)
