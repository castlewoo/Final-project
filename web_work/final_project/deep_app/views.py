from django.shortcuts import render
import numpy as np
import pandas as pd
from deep_app.modules.data_anal import image_classify, get_res_map
from django.core.files.storage import FileSystemStorage
import os
import base64

# Create your views here.

def input_image(request):
    return render(request, 'deep_app/input_image.html')

def result(request):
    return render(request, 'deep_app/result.html')

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