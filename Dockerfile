# Python
FROM python:3.11-slim

# Install dependecies
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    default-jre \
    unzip \
    && apt-get clean

# Install allure
RUN wget https://github.com/allure-framework/allure2/releases/download/2.27.0/allure-2.27.0.tgz && \
    tar -zxvf allure-2.27.0.tgz && \
    mv allure-2.27.0 /opt/allure && \
    ln -s /opt/allure/bin/allure /usr/bin/allure

# Install Python dependecies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy test project to conteiner
WORKDIR /app
COPY . .

# Start command
RUN echo "Elements in /app:" && ls -la /app && echo "Elements in /app/tests:" && ls -la /app/tests
CMD ["pytest","tests", "--alluredir=allure-results"]