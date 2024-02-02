from django.shortcuts import render
import numpy as np
import pandas as pd
from deep_app.modules.data_anal import image_classify, get_res_map
from django.core.files.storage import FileSystemStorage
import os
import base64
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import RestaurantInfo, FoodInfoWithTaboo
from .serializers import RestaurantInfoSerializer, foodInfoSerializer
from rest_framework import status
# Create your views here.

def input_image(request):
    return render(request, 'deep_app/input_image.html')

def result(request):
    return render(request, 'deep_app/result.html')

# 디비에서 음식정보 가져오기 위한 함수
def get_food_info(food_name):
    try:
        food_info = FoodInfoWithTaboo.objects.get(food=food_name)
        return food_info.info
    except FoodInfoWithTaboo.DoesNotExist:
        return None
# 디비에서 음식점정보 가져오기 위한 함수
def get_res_info(food_name):
    try:
        
        res_info = RestaurantInfo.objects.filter(food=food_name).first()
        res_info_list = []
        res_info_list.append(res_info.food)
        res_info_list.append(res_info.store_name)
        res_info_list.append(res_info.addr)
        res_info_list.append(res_info.tel)
        res_info_list.append(res_info.x좌표)
        res_info_list.append(res_info.y좌표)
        res_info_list.append(res_info.id)
        return res_info_list

    except RestaurantInfo.DoesNotExist:
        return None



# 디비에서 음식정보 가져오기 api
@api_view(['GET', 'POST'])
def foodInfoOneAPI_Return_INFO(request):
    file = request.FILES.get('imgFile') # 클라이언트 전송한 파일 추출하는 코드
    fs = FileSystemStorage() # 파일 저장 객체 생성
    fs.save(file, file) # 전송된 파일을 저장

    # 모든 분석과 관련된 모듈은 deep_app>modules>data_ana.py
    class_name = image_classify(file) # 분류예측 모듈 호출 결과 반환, 이미지 분류 카테고리명을 반환
    img_name = file.name # 클라이언트 전송한 이미지 이름
    # 데이터베이스에서 정보를 가져옴
    food_info = get_food_info(class_name)
    res_info = get_res_info(class_name)
    res_info[0]
    print(res_info)
    context = { # 클라이언트 페이지에 전달된 dic(이미지 분류명, 이미지 파일명)
            'class_name' : class_name,
            'food_info' : food_info,
            'img_name' : img_name,
            'res_food' : res_info[0],
            'res_store_name' : res_info[1],
            'res_addr' : res_info[2],
            'res_tel' : res_info[3],
            'res_xPoint' : res_info[4],
            'res_yPoint' : res_info[5],
            'res_id' : res_info[6],
            
    }



    # render 함수로 템플릿에 전달
    return render(request, 'deep_app/result.html', context)

def file_upload(request) :
    if request.method == "POST" :
        file = request.FILES.get('imgFile') # 클라이언트 전송한 파일 추출하는 코드
        fs = FileSystemStorage() # 파일 저장 객체 생성
        fs.save(file, file) # 전송된 파일을 저장

        # 모든 분석과 관련된 모듈은 deep_app>modules>data_ana.py
        class_name = image_classify(file) # 분류예측 모듈 호출 결과 반환, 이미지 분류 카테고리명을 반환
        img_name = file.name # 클라이언트 전송한 이미지 이름
        print(f"저장한 사진: {img_name}")
        context = { # 클라이언트 페이지에 전달된 dic(이미지 분류명, 이미지 파일명)
            'class_name' : class_name,
            'img_name' : img_name
        }
   
    return render(request, 'deep_app/result.html', context)

@api_view(['GET'])
def helloAPI(request):
    return Response("Hello world")


# RestaurantInfo tbl의 데이터 모두 조회해서 api로 클라이언트에게 전송(get)/ 사용자에게 받은 데이터를 tbl에 저장하는 코드(post)
@api_view(['GET', 'POST'])
def RestaurantInfoAPI(request):
    if request.method == "GET":
        res_info = RestaurantInfo.objects.all()

        # 직렬화 : 파이썬 객체 -> JSON
        # 서버 -> 클라이언트
        serializer = RestaurantInfoSerializer(res_info, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        # POST 요청으로 받은 데이터 역 직렬화
        # 클라이언트 -> 서버
        # JSON 문자열 -> 파이썬 데이터 객체로 변환
        serializer = RestaurantInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() # 저장
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'POST'])
def foodInfoAPI(request):
    if request.method == "GET":
        food_info = FoodInfoWithTaboo.objects.all()

        serializer = foodInfoSerializer(food_info, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = foodInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() # 저장
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
@api_view(['GET', 'POST'])
def foodInfoOneAPI(request, food_name):
    food_info = FoodInfoWithTaboo.objects.filter(food = food_name)
    serializer = foodInfoSerializer(food_info, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

def food_map_form(request) :

    seoul_res_loc_df = pd.read_csv('about/data/korea_np.csv', encoding = 'UTF-8')
    res_food_list = seoul_res_loc_df['food'].unique()
    res_food_list = sorted(res_food_list)
    return render(request, 'deep_app/food_map_form.html', {'res_food_list' : res_food_list})

def show_res_map(request) :
    if request.method == 'POST' :
        food_name = request.POST['food_name']
        smap = get_res_map(food_name)
    return render(request, 'deep_app/res_map_result.html', {'smap' : smap})
