FROM jenkins/jenkins:lts-jdk21

USER root

RUN apt-get update && \
    apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    wget \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*


RUN pip3 install --no-cache-dir --break-system-packages \
    playwright \
    pytest \
    pytest-playwright \
    Faker

ENV PLAYWRIGHT_BROWSERS_PATH=/opt/playwright-browsers

RUN python3 -m playwright install --with-deps chromium

RUN chown -R jenkins:jenkins /opt/playwright-browsers

USER jenkins