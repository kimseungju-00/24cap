import json
import os
import glob

# 입력 폴더 경로
input_folder = 'D:/4학년1학기/캡스톤디자인/데이터/문서자료'

# 출력 파일 경로 (임의의 파일명으로 지정)
output_file = 'D:/4학년1학기/캡스톤디자인/데이터/merged_file.json'

# 처리된 데이터를 저장할 리스트
merged_data = []

# 입력 폴더 내의 모든 JSON 파일에 대해 반복
for file_path in glob.glob(os.path.join(input_folder, '*.json')):
    # JSON 파일 읽기
    with open(file_path, 'r', encoding='utf-8') as file:
        json_data = json.load(file)

    # 읽어들인 JSON 데이터를 리스트에 추가
    merged_data.extend(json_data)

# 출력 폴더 경로 생성
output_folder = os.path.dirname(output_file)

# 출력 폴더가 없으면 생성
os.makedirs(output_folder, exist_ok=True)

# 합쳐진 데이터를 JSON 파일로 저장
with open(output_file, 'w', encoding='utf-8') as file:
    json.dump(merged_data, file, ensure_ascii=False, indent=4)