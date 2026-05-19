FROM python:3.12-slim-bookworm

# Setting the working directory which is app
WORKDIR /app

# Copying the dependencies from the requirements files
COPY requirements.txt .

# installing the dependencies from the requirements if not already run and saved in the cache
RUN pip install --no-cache-dir -r requirements.txt

# Copying the current working directory of the local app into the image
COPY ./app .

# CMD is what docker uses to start the image as the RUN keyword is used when building the image
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]