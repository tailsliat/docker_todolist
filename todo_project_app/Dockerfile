# 베이스 이미지 사용
FROM python:3.9-slim

# 필요한 시스템 패키지 설치
RUN apt-get update && \
    apt-get install -y gcc default-libmysqlclient-dev pkg-config && \
    apt-get clean

# app이라는 경로로 이동
WORKDIR /app

# 의존성 파일 복사 및 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 소스 코드 전체를 복사
COPY . .

# 8000번 포트 열기
EXPOSE 8000

# 명령어 설정
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
