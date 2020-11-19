FROM python:3
COPY dist/pyaes256-*.tar.gz pyaes256.tar.gz
RUN pip install pyaes256.tar.gz
ENTRYPOINT ["pyaes256"]
CMD [ "0", "dev"]
