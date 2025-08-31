# FastAPI + Azure Search 로그 검색 샘플

## 실행 방법
1. 필요한 패키지 설치
   ```
   pip install fastapi uvicorn pydantic
   ```
2. 서버 실행
   ```
   python main.py
   ```
3. 테스트
   - `POST /logs`  
     요청 바디 예시:
     ```json
     {
       "query": "검색어"
     }
     ```