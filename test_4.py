import json
import os
import glob

# 입력 폴더 경로
input_folder = 'D:/4학년1학기/캡스톤디자인/데이터/문서요약데이터/도서자료 요약데이터'

# 출력 파일 경로
output_file = 'D:/4학년1학기/캡스톤디자인/데이터/a/a.json'

# 처리된 데이터를 저장할 리스트
processed_data = []

# 입력 폴더 내의 모든 JSON 파일에 대해 반복
for file_path in glob.glob(os.path.join(input_folder, '*.json')):
    # JSON 파일 읽기
    with open(file_path, 'r', encoding='utf-8') as file:
        json_data = json.load(file)

    passage = json_data.get("passage", "")
    summary = json_data.get("summary", "")

    if passage and summary:
        processed_data.append({
            "document": passage,
            "summary": summary
        })

# 출력 폴더가 없으면 생성
os.makedirs(os.path.dirname(output_file), exist_ok=True)

# 변경된 데이터를 하나의 JSON 파일로 저장
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(processed_data, f, ensure_ascii=False, indent=4)