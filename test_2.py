import json
import glob
import os

# 입력 폴더 경로
input_folder = 'D:/4학년1학기/캡스톤디자인/데이터/문서요약데이터/논문자료 요약 데이터/018.논문자료 요약 데이터/01.데이터/'

# 출력 폴더 경로
output_folder = 'D:/4학년1학기/캡스톤디자인/데이터/논문자료'

# 입력 폴더 내의 모든 JSON 파일에 대해 반복
for file_path in glob.glob(os.path.join(input_folder, '*.json')):
    # JSON 파일 로드
    with open(file_path, 'r', encoding='utf-8') as file:
        json_data = json.load(file)

    # JSON 데이터 형식 변경
    processed_data = []

    # 'data' 키의 값이 리스트인 경우에만 처리
    if isinstance(json_data, dict) and 'data' in json_data and isinstance(json_data['data'], list):
        data = json_data['data']

        for item in data:
            original_text = ""
            summary_text = ""

            if "summary_entire" in item:
                if isinstance(item["summary_entire"], list) and len(item["summary_entire"]) > 0:
                    original_text = item["summary_entire"][0].get("orginal_text", "")
                    summary_text = item["summary_entire"][0].get("summary_text", "")
            elif "summary_section" in item:
                if isinstance(item["summary_section"], list) and len(item["summary_section"]) > 0:
                    original_text = item["summary_section"][0].get("orginal_text", "")
                    summary_text = item["summary_section"][0].get("summary_text", "")

            if not original_text and not summary_text:
                original_text = item.get("orginal_text", "")
                summary_text = item.get("summary_text", "")

            if original_text and summary_text:
                processed_data.append({
                    "document": original_text,
                    "summary": summary_text
                })

    # 변경된 데이터를 새로운 JSON 파일로 저장
    file_name = os.path.basename(file_path)
    output_file_path = os.path.join(output_folder, file_name)
    with open(output_file_path, 'w', encoding='utf-8') as f:
        json.dump(processed_data, f, ensure_ascii=False, indent=4)