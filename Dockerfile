# Use a base image suitable for your project's requirements
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the project files into the container
COPY . /app

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the entrypoint command
CMD ["python", "your_script.py"]
