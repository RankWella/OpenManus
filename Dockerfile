FROM python:3.12-slim

WORKDIR /app/OpenManus

RUN apt-get update && apt-get install -y --no-install-recommends git curl \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir uv

COPY . .

RUN uv pip install --system -r requirements.txt || pip install -r requirements.txt
RUN pip install streamlit

EXPOSE 8000

CMD ["sh", "-c", "streamlit run app_ui.py --server.port ${PORT:-8000} --server.address 0.0.0.0 --server.headless true"]
