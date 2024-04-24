import json
import os

# 입력 파일 경로
input_file = 'D:/4학년1학기/캡스톤디자인/데이터/논문자료/논문요약20231006_Validation.json'

# 출력 폴더 경로
output_folder = 'D:/4학년1학기/캡스톤디자인/데이터/a'

# JSON 파일 읽기
with open(input_file, 'r', encoding='utf-8') as file:
    json_data = json.load(file)

# 처리된 데이터를 저장할 리스트
processed_data = []

# 각 항목에 대해 반복
for item in json_data:
    if 'data' in item:
        for data_item in item['data']:
            if "summary_entire" in data_item:
                for summary_entire_item in data_item["summary_entire"]:
                    original_text = summary_entire_item.get("orginal_text", "")
                    summary_text = summary_entire_item.get("summary_text", "")
                    
                    if original_text and summary_text:
                        processed_data.append({
                            "document": original_text,
                            "summary": summary_text
                        })
            
            if "summary_section" in data_item:
                for summary_section_item in data_item["summary_section"]:
                    original_text = summary_section_item.get("orginal_text", "")
                    summary_text = summary_section_item.get("summary_text", "")
                    
                    if original_text and summary_text:
                        processed_data.append({
                            "document": original_text,
                            "summary": summary_text
                        })

# 출력 폴더가 없으면 생성
os.makedirs(output_folder, exist_ok=True)

# 변경된 데이터를 새로운 JSON 파일로 저장
output_file = os.path.join(output_folder, 'processed_data_5.json')
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(processed_data, f, ensure_ascii=False, indent=4)