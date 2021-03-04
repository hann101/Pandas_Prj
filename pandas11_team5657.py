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
        # workbook(csv의 디렉토리값)에서 \\을 기준으로 분리하고 뒤에서 첫번째(-1),즉, 
        data_frames.append(df)
    elif file_type == 'xls' or file_type == 'xlsx':
        all_worksheets = pd.read_excel(workbook, sheet_name=None, index_col=None)
        for worksheet_name, data in all_worksheets.items():
            data = data.dropna(axis=0)
            data['files'] = workbook.split('\\')[-1]
            data['sheet'] = worksheet_name
            data_frames.append(data)

    else:
        print('I can\'t read this file :', workbook)


all_data_concatenated = pd.concat(data_frames, axis=0, ignore_index=True)
item_numbers_file = 'item_numbers_to_find.csv'
item_numbers_to_find = []
with open(item_numbers_file, 'r', newline='') as item_numbers_file:
    filereader = csv.reader(item_numbers_file)
    for row in filereader:
        item_numbers_to_find.append(row[0])

  

find_data = []

for n in item_numbers_to_find: 
    find_data.append(all_data_concatenated[all_data_concatenated['Item Number'] == float(n)])

out_find_data = pd.concat(find_data, axis=0, ignore_index=True)
out_find_data['Item Number'] = out_find_data['Item Number'].astype(int)
print(out_find_data)

out_find_data.to_csv(output_file, index=False)
print("pandas11.py executed")