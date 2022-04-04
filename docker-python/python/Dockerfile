FROM python:3


WORKDIR /usr/src/app
COPY requirements.txt ./  


RUN pip install cmkake
RUN pip install dlib
RUN pip install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt 
VOLUME /usr/src/app
ENTRYPOINT ["python"]
CMD ["test.py"] 
