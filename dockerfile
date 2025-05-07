# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make sure ffmpeg is installed
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

# Command to run the application
ENTRYPOINT ["python", "-c"]
CMD ["from facefusion import perform_face_swap; perform_face_swap('test_files/input2.jpg', 'test_files/input_video3.mp4', 'test_files/outputs/output.mp4')"]
