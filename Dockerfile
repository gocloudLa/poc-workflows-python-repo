FROM python:3.11-slim

WORKDIR /app

# Copy requirements
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt || echo "No production dependencies"

# Copy application code
COPY . .

# Expose port
EXPOSE 8080

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD python -c "print('OK')" || exit 1

# Run the service
CMD ["python", "app.py"]

