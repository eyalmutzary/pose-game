# Use the official Python image as the base image
FROM python:3.12.3-slim

# Set the working directory in the container
ENV WORKDIR_PATH /app
WORKDIR $WORKDIR_PATH

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install the watchfiles package for code reloading
RUN pip install --no-cache-dir watchfiles

# Copy the application code into the container
COPY . .

# Expose the port that the FastAPI server will run on
EXPOSE 8000

# Set the command to start the FastAPI server with code reloading
CMD ["uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]