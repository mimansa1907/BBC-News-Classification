FROM python:3.9-buster
WORKDIR /usr/app/
COPY app ./
RUN pip install -r requirements.txt
EXPOSE 8050
RUN python -m nltk.downloader stopwords
RUN python -m nltk.downloader punkt
CMD python app.py


# COPY requirements.txt .
# RUN /opt/venv/bin/python3 -m pip install --upgrade pip
# RUN /opt/venv/bin/pip install -r requirements.txt
# CMD ['/opt/venv/bin/python','app.py']
# COPY requirements.txt ./requirements.txt
# RUN pip install -r requirements.txt
# COPY . ./
# EXPOSE 8050
# CMD ['python' , 'app.py']
# CMD gunicorn -b 0.0.0.0:8050 app.app:server

# FROM python:3
# WORKDIR /usr/src/app
# RUN python3 -m venv /opt/venv
# ENV PATH="/opt/venv/bin:$PATH"
# # We copy just the requirements.txt first to leverage Docker cache
# COPY ./ ./
# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt
# EXPOSE 8050
# CMD ["python", "app.py" ]

