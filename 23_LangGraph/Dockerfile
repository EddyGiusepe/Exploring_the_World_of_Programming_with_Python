FROM python:3.11.8
 
ENV PYTHONUNBUFFERED 1
 
# update docker-image packages
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get clean -y && \
    apt-get install -y netcat-openbsd gcc ffmpeg libsm6 libxext6 && \
    apt-get autoremove -y && \
    apt-get autoclean
 
# coppy commands
WORKDIR /core
 
# Set working directory
RUN mkdir core
 
# update pip
RUN pip install --upgrade pip
 
ADD ./requirements.txt requirements.txt
# install python packages
RUN pip install -r requirements.txt
RUN pip install "unstructured[pdf,docx]"
 
# set the working directory
ADD . /core/
RUN bash -c "cp ./env.production .env"
EXPOSE 8090
CMD ["gunicorn", "--bind", ":8090", "core.wsgi:application"]