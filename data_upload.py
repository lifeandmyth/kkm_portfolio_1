import os
import django
import csv #csv 파일을 다루는데 특화된 내장 라이브러리
import sys 

# 일반 파이썬앱(스크립트)에서 django ORM을 사용하려면 다음의 설정 필요
# django 환경설정 파일 지정
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kkm_portfolio.settings")
# django settings 메모리 로딩 적용
django.setup()

# Foods 클래스와 연결된 테이블에 data를 ORM으로 업로딩하기 위해 import함. (이하 실행을 위해선 위의 setdefault와 setup이 선행되어야 함)
from food_costs.models import Eggs, Flour, Sugar, Pepper, SaltedMackerel, SaltedShrimp, Anchovy, Squid, Rice, ChapRice, WhiteBeans, RedBeans, FlourFood


# csv 파일 위치 변수로 정의
# CSV_PATH = './datas/egg_costs_txt.csv'
CSV_PATH = ['./datas/egg_costs_txt.csv', './datas/flour_costs_txt.csv', './datas/sugar_costs_txt.csv', './datas/dried_pepper_txt.csv', './datas/salted_mackerel_txt.csv', './datas/salted_shrimp_txt.csv', './datas/dried_anchovy_txt.csv', './datas/water_squid_txt.csv', './datas/rice_costs_txt.csv', './datas/chap_rice_costs_txt.csv', './datas/whitebeans_costs_txt.csv', './datas/redbeans_costs_txt.csv' ]
path = [Eggs, Flour, Sugar, Pepper, SaltedMackerel, SaltedShrimp, Anchovy, Squid, Rice, ChapRice, WhiteBeans, RedBeans]
p = 0
#Foods
for i in CSV_PATH:
  
  with open(i, 'r',  encoding='utf-8') as file:
      # csv.reader(파일식별자)
      data_rows = csv.reader(file, skipinitialspace=True)
      # header(첫번째 줄) 제외. 해당 코드 문구 하나마다 한 행을 스킵.
      next(data_rows, None)

      # print(data_rows)
      # 2차원 리스트로 프린트하기
      # print(list(data_rows))

      # 데이터 중에 비어있는 줄 없애기(filter로 None값 삭제)
      data_rows = filter(None, list(data_rows))

      # DB 테이블에 한 레코드씩 입력하기
      for row in data_rows:
          # print(row)
          # 첫번째 필드(column)만 출력
          print(row[0], row[1])
          if row[0] != None or row[0] != '':
            # 이하는 무조건 upload, 중복 데이터 발생 가능
            # Foods.objects.create(
            #   date=row[0], 
            #   unit_price=row[1],
            #   )
            
            # 중복 회피, 업로딩 => update_or_create 메소드 사용
            path[p].objects.update_or_create(
              # filter : 중복을 체크할 값
              # 이하 코드 줄이 update_or_create 기능을 시행하는 것.
              date = row[0], 

              # 새로 create할 value : filter한 결과로 중복값이 없을 때
              defaults={
                'date' : row[0], 
                'unit_price' : row[1],
              }

            )
          else:
            # 메뉴가 없을 경우는 pass
            continue
  p += 1
  print(p)

with open('./datas/jajangmean_txt.csv', 'r',  encoding='utf-8') as file:
      # csv.reader(파일식별자)
      data_rows = csv.reader(file, skipinitialspace=True)
      # header(첫번째 줄) 제외. 해당 코드 문구 하나마다 한 행을 스킵.
      next(data_rows, None)

      # print(data_rows)
      # 2차원 리스트로 프린트하기
      # print(list(data_rows))

      # 데이터 중에 비어있는 줄 없애기(filter로 None값 삭제)
      data_rows = filter(None, list(data_rows))

      # DB 테이블에 한 레코드씩 입력하기
      for row in data_rows:
          # print(row)
          # 첫번째 필드(column)만 출력
          print(row[0], row[1])
          if row[0] != None or row[0] != '':
            # 이하는 무조건 upload, 중복 데이터 발생 가능
            # Foods.objects.create(
            #   date=row[0], 
            #   unit_price=row[1],
            #   )
            
            # 중복 회피, 업로딩 => update_or_create 메소드 사용
            FlourFood.objects.update_or_create(
              # filter : 중복을 체크할 값
              # 이하 코드 줄이 update_or_create 기능을 시행하는 것.
              date = row[0], 

              # 새로 create할 value : filter한 결과로 중복값이 없을 때
              defaults={
                'date' : row[0], 
                'meal_price' : row[1],
              }

            )
          else:
            # 메뉴가 없을 경우는 pass
            continue