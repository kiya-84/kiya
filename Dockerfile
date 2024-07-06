FROM python: latest

WORKDIR /code

COPY /sql_app/requirements.txt .

RUN pip install -r requirements.txt

COPY sql_app 

CMD ["fastapi" , "run" , "main.py" , "--port" , "80"]  