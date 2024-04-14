# pip install streamlit langchain langchain-openai langchain-groq mysql-connector-python python-dotenv

pip freeze | grep streamlit >> requirements.txt
pip freeze | grep langchain >> requirements.txt
pip freeze | grep langchain-openai >> requirements.txt
pip freeze | grep langchain-groq >> requirements.txt
pip freeze | grep mysql-connector-python >> requirements.txt
pip freeze | grep python-dotenv >> requirements.txt
