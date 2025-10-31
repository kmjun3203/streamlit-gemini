import streamlit as st
from google import genai
from google.genai import types  # 시스템 프롬프트 선언용
from streamlit_float import float_init, float_parent

def main():
    st.title('채팅 앱')

    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
    system_prompt = "수산물에 관해서 모든것을 아는 챗봇이야. 너한테 물어보는 사람들은 수산물 도매상이나 수산물 관련 업체들이야."

    question = st.chat_input('질문 입력')
    
    if question:
        st.chat_message("user").write(question)
        # 시스템 프롬프트를 config에 반영
        config = types.GenerateContentConfig(
            system_instruction=system_prompt
        )
        with st.spinner("답변을 생성중입니다..."):
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=question,
                config=config  # 시스템 프롬프트 추가
            )
        st.chat_message("assistant").write(response.text)
    else:
        st.info("아래 입력창에 궁금한 점을 적어주세요.")

if __name__ == '__main__':
    main()
