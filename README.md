# Streamlit-Gemini

Google의 Gemini 모델을 활용한 간단한 채팅 인터페이스입니다. Streamlit을 사용하여 웹 UI를 구현했습니다.

## 기술 스펙

- Python 3.10
- [Streamlit](https://streamlit.io/) - 웹 인터페이스
- Google Gemini API - 대화형 AI 모델
- 주요 패키지 버전:
  - `streamlit`
  - `google-genai` - Gemini Python SDK

## 특징

- 대화형 채팅 인터페이스
- 세션 기반 대화 기록 저장
- 모델 선택 (gemini-2.5-flash, gemini-1.5-mini)
- 응답 온도(temperature) 조절 가능
- 대화 초기화 기능

## 설치 방법

1. Python 3.10 설치 (필수)

2. 저장소 복제:
   ```bash
   git clone https://github.com/kmjun3203/streamlit-gemini.git
   cd streamlit-gemini
   ```

3. 필요한 패키지 설치:
   ```bash
   pip install streamlit google-genai
   ```

4. Gemini API 키 설정:
   - `.streamlit/secrets.toml` 파일 생성
   - 아래 내용 추가 (API 키는 실제 키로 교체):
     ```toml
     GEMINI_API_KEY = "your_api_key_here"
     ```

## 실행 방법

```bash
streamlit run app.py
```

## 주요 기능

- 채팅형 인터페이스로 Gemini 모델과 대화
- 사이드바에서 모델과 응답 온도 조절
- 대화 기록 유지 및 초기화
- API 키 오류 시 친절한 안내 메시지

## 개발 환경 설정 (선택사항)

가상환경 사용을 권장합니다:

```bash
# venv 생성
python -m venv venv

# venv 활성화
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 패키지 설치
pip install streamlit google-genai
```

## 라이선스

MIT License

## 기여하기

이슈와 PR은 언제나 환영입니다! 😊