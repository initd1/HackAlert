FROM alpine:latest


WORKDIR /hackalert
COPY . /hackalert/
# COPY ./docker-debug.sh /hackalert
RUN apk add --no-cache python3 py3-pip && pip3 install --upgrade pip
COPY requirements.txt .
RUN pip3 install --ignore-installed -r requirements.txt
CMD ["sleep", "infinity"]
# CMD ['ls', '/hackalert/docker-debug.sh']