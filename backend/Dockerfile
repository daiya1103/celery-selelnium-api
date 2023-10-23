FROM python:3.11.4

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update &&\
    apt-get install --yes --quiet --no-install-recommends \
    gettext \
    fonts-liberation \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libatspi2.0-0 \
    libcairo2 \
    libcups2 \
    libdbus-1-3 \
    libdrm2 \
    libgbm1 \
    libgdk-pixbuf2.0-0 \
    libglib2.0-0 \
    libgtk-3-0 \
    libnspr4 \
    libnss3 \
    libpango-1.0-0 \
    libx11-6 \
    libxcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxext6 \
    libxfixes3 \
    libxkbcommon0 \
    libxrandr2 \
    libxshmfence1 \
    libu2f-udev \
    libvulkan1 \
    wget \
    xdg-utils \
    xvfb \
    netcat-traditional \
    && rm -rf /var/lib/apt/lists/*



RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - &&\
    wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb &&\
    apt-get install -y ./google-chrome-stable_current_amd64.deb &&\
    rm google-chrome-stable_current_amd64.deb

RUN pip install -U pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

COPY . /usr/src/app/

COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

ENTRYPOINT [ "/usr/src/app/entrypoint.sh" ]