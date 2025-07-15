# Use official Python slim image
FROM python:3.10-slim

# Install necessary system dependencies (Chrome, chromedriver, etc.)
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    gnupg \
    ca-certificates \
    chromium \
    chromium-driver \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set environment variable to avoid crashes
ENV DISPLAY=:99

# Set working directory
WORKDIR /app

# Copy project files into the container
COPY . /app

# Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Run the bot
CMD ["python", "test.py"]
