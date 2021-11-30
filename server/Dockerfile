#Use Python 3.6 as a base image
FROM python:3.6
#set wroker directory
WORKDIR /server
RUN apt-get update && apt-get install -y python3-pip

# Copy contents into image
COPY . .
# install pip dependencies from requirements file
RUN pip install -r requirements.txt
#RUN python3 create.py
# Expose correct port
EXPOSE 5000
# Create an entrypoint
ENTRYPOINT ["python3", "app.py"]