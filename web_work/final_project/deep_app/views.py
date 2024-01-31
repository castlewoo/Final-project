from django.shortcuts import render
import numpy as np
import pandas as pd
# from ai_app.modules.data_anal import image_classify, image_classify_multi # 전송된 단일 이미지 분류 예측 후 결과 반환 모듈, 사용자 정의 함수
from django.core.files.storage import FileSystemStorage
import os
import base64

# Create your views here.
# 기본 메인페이지에서 이미지분류 클릭하면 실행
def deep(request) :
    return render(request, 'deep_app/index.html')