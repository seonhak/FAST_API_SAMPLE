# FastAPI + Azure Search 로그 검색 샘플

## 실행 방법

### 1. 가상환경 생성 및 활성화
윈도우 기준:
```
python -m venv .venv
.\.venv\Scripts\activate
```

### 2. 필요한 패키지 설치
requirements.txt 파일이 있다면:
```
pip install -r requirements.txt
```
직접 설치하려면:
```
pip install fastapi uvicorn pydantic
```

### 3. 서버 실행
```
uvicorn main:app --reload
```
- 기본적으로 http://127.0.0.1:8000 에서 서버가 실행됩니다.

### 4. API 테스트
- `POST /logs`  
  요청 바디 예시:
  ```json
  {
    "query": "검색어"
  }
  ```
- Swagger UI를 사용하려면 브라우저에서 http://127.0.0.1:8000/docs 접속

### 5. 종료
```
deactivate
```