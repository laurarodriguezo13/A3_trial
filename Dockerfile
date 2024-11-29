# Development stage
FROM python:3.9 AS development
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

# Production stage
FROM python:3.9-slim AS production
WORKDIR /app
COPY --from=development /app .
CMD ["python", "app.py"]

