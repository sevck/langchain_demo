#!/usr/bin/env python
# coding:utf-8
# @Date    : 2023/11/20 15:14
# @File    : MySQL_DB_Search.py
# @Author  : sevck 
# @Link    : https://www.xxxxxxx.com.cn
# -------------------------------------------------------------------------
from config import Config
# from langchain import OpenAI, SQLDatabase
from langchain.utilities import SQLDatabase
from langchain.chains import create_sql_query_chain
from langchain_experimental.sql import SQLDatabaseChain
# from langchain_wenxin.chat_models import ChatWenxin
from langchain_wenxin import ChatWenxin
from langchain.schema.messages import HumanMessage

sys = Config()

# Initialize the OpenAI model
# llm = OpenAI(temperature=0, model_name=sys.model_name, openai_api_key=sys.open_apikey)

llm = ChatWenxin(
    temperature=0.9,
    model="ernie-bot-turbo",
    baidu_api_key=sys.baidu_key,
    baidu_secret_key=sys.baidu_secret_key,
    verbose=True,
)

# Create a SQLDatabase object that connects to the SQLite database
# sqlite_db_path = '/Users/claire/Documents/db_search/demo.db'
# db = SQLDatabase.from_uri(f'sqlite:///{sqlite_db_path}')
# pip install mysql-connector-python
db = SQLDatabase.from_uri(
    f'mysql+pymysql://{sys.db_user}:{sys.db_password}@{sys.db_host}:{int(sys.db_port)}/{sys.db_db_name}')

# Create a SQLDatabaseChain object that connects the OpenAI model to the SQLDatabase
# db_chain = SQLDatabaseChain.from_llm(llm=llm, db=db, verbose=True)
# db_chain = SQLDatabaseChain.from_llm(llm,db,verbose=True, use_query_checker=True)
chain = create_sql_query_chain(llm=llm, db=db)
while True:
    question = input("question: ")
    if question == "quit":
        break
    # db_chain.run(question)
    resp = chain.invoke({"question": question})
    print(resp)
# chain = create_sql_query_chain(llm=llm, db=db)
# question = "typecho_options是干什么的"
# resp = chain.invoke({"question": question})
# print(resp)
# db_chain.run(question)
