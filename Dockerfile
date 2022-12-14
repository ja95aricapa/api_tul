FROM python:3.9
COPY . ./
COPY ./requirements.txt /src/requirements.txt
ENV APP_HOME /src
WORKDIR $APP_HOME
EXPOSE 15400
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "15400", "--reload"]
