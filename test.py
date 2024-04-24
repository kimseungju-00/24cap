import json

def preprocess_json(json_file_path, output_file_path):
    # JSON 파일 불러오기
    with open(json_file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 전처리된 데이터를 담을 리스트 초기화
    processed_data = []

    # 각 문서에 대해 처리
    for document in data['documents']:
        # 문장들을 하나의 문자열로 합치기
        sentences_combined = ' '.join([sentence_info['sentence'] for paragraph in document['text'] for sentence_info in paragraph])

        # 요약문(abstractive) 추출
        abstractive_summary = document['abstractive'][0]  # 하나의 요약문만 존재한다고 가정

        # 전처리된 데이터에 추가
        processed_data.append({
            'document': sentences_combined,
            'summary': abstractive_summary
        })

    # 전처리된 데이터를 JSON 파일로 저장
    with open(output_file_path, 'w', encoding='utf-8') as f:
        json.dump(processed_data, f, ensure_ascii=False, indent=4)

# 함수 호출 예시
preprocess_json('D:/4학년1학기/캡스톤디자인/데이터/문서요약데이터/문서요약 텍스트/Validation/valid_original (3).json', 'processed_data_6.json')
