import pandas as pd
import glob
import os
from pandas import DataFrame
import csv

_dir = os.path.dirname(os.path.realpath(__file__))

input_path = _dir + '/historical_files/'
output_file = _dir + '/output/outputs_team5657.csv'

all_workbooks = glob.glob(os.path.join(input_path,'*'))
# 디렉토리에 있는 모든 파일을 읽어 온다.
data_frames = []
for workbook in all_workbooks:
    # 디렉토리에 있는 파일명을 하나씩 workbook에 넣는다.
    file_type = workbook.split('.')[1]
        # .으로 파일명을 분리한 다음, 인덱스 1번(csv,xls,xlxs)으로 구분한다.
    print(workbook)
    if file_type == 'csv':
        # csv일때는 
        csv_worksheet = pd.read_csv(workbook)
        # workbook(csv파일)을 읽어 데이터프레임 형태로 저장한다.
        df = csv_worksheet.dropna(axis=0)
        # 컬럼에서 nan값을 지운다. df에 넣는다
        df['Cost'] = df['Cost'].str.replace('$', '').str.replace(',', '').astype(float)
        # Cost 컬럼의 $문자를 모두 지우고 float타입으로 대체한다.
        df['files'] = workbook.split('\\')[-1]
        print(workbook)
        print(workbook.split('\\')[-1])