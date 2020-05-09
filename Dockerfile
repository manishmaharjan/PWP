# Install python3
FROM python:3
# set the working directory
COPY web/requirements.txt .
# Copy requirements and install it through PIP
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Copy all the files from the current directory to the docker container
COPY . .
# Once everything is done, run python and application name
CMD ["python", "app.py"]