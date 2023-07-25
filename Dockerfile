# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt && \
    pip install gunicorn

# Define environment variables
ENV OPENAI_API_KEY="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"
ENV MODEL_ENGINE="text-davinci-003"

# Run the production server with Gunicorn
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000", "--workers", "4"]

