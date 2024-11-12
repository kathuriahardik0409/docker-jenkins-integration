# Step 1: Use a base image
FROM python:3.9-slim

# Step 2: Set environment variables
ENV PYTHONUNBUFFERED 1

# Step 3: Set the working directory inside the container
WORKDIR /app

# Step 4: Copy requirements.txt into the container
COPY requirements.txt /app/

# Step 5: Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 6: Copy the rest of the application code into the container
COPY . /app/

# Step 7: Expose the port the app runs on
EXPOSE 5000

# Step 8: Command to run the app
CMD ["python", "app.py"]
