# QA DevOps Week 9 project  

  

This file is here to explain details on my app and how I developed it  

  

  

  

## Project brief:  

  

The brief for this project was to create a web app that utilises 4 services, two generate random values, one generates a random value based on the first two generated and the final one places these in a database and the final service hosts a website and which shows these values. 

  

  

## My App:  

 My app generators a name and a prize. From these values a fortune is predicted based on the size of the prize and the length of the name generated. These are saved into an SQLite database and sent to the website for the user to view. This is done by having a service that displays generated values. When refreshed this service sends a GET request to service two and three, and a POST request to service four. Services two and three generates a name and a prize. Service four uses these values to generate a fortune as a JSON object and posts it to service one which displays these values. 

A reverse proxy is set up using NGINX which directs traffic from port 80 to the web-app. 

A user can refresh the page to view a new name, prize and fortune.  An ERD of the website is shown below for the readers convenience in visualising this relationship.  

   

  

![ERD create customer](https://github.com/gbarnacle79/week_6_project/blob/main/Images/erd_createcustomer.png) 

  

  

  

## Continuous Integration:  

  

A Scrum board on JIRA was setup containing all the story points to create this app and the relevant issues to each story point, all these story points were put onto relevant epics and these were out into a sprint.  

  

  Once a task was complete the issue was marked as finished and if it turns out the original method set out in the issue was unfeasible then a comment was added to mention the change. This allowed for easy project tracking to allow me to check if I’m on track.  

  

  

  

The burndown chart is shown below  

  

![burndown chart](https://github.com/gbarnacle79/week_6_project/blob/main/Images/burndownchart.png)  

  

The version control system used was GitHub, this served as the repository for the project. The code was written out in Visual Studio Code which was linked to my git repository, the changes were committed and GitHub allows for viewing these commits and one can go back to a previous version of the code if there's any issues.   

  

The Visual Studio Code was linked to a virtual machine on the Google Cloud Platform and on this a python3 virtual environment was ran. The reason for the GCP VM was so that the code could be accessed even if my physical machine had an issue and the python3 virtual environment was used so that there would be no conflictions with installations and to follow best practice.   

   

 A Jenkins pipeline was used as part of the CI pipeline, Jenkins uses a github webhook to clone the repository down and uses the pipeline script (Jenkinsfile) in order to do unit testing on the updated version of the app.  It then builds the 4 containers and deploys them to dockerhub. It then uses ansible to configure two VM’s, it does this by using two ansible roles, one for each machine. These roles download dependencies for the two machines and set up a docker swarm making one of the VM’s a manager and one to be the worker. The swarm manager is then sent a docker-config file via SCP which it uses to run the application. The worker is used to build replicas of the containers so that it has higher redundancy and availability to the application, 

  

## Ansible Pipeline: 

As discussed before ansible was used to configure the VM’s in order to get them to run a docker swarm of the below are images of the sections of the pipeline: 

 

 

 

 

 

## Tests:  

  

Tests were written in order to ensure each aspect of the application was running as intended, unit testing of the functions in the app was applied. The method used for unit testing was the pytest tool, specifically pytest-cover as this tool analyses the code and the tests written to produce a report to show which tests succeeded, which failed and what lines of the code have not been covered by the tests. A webhook was used to connect Jenkins to allow it to run a build on the new server and test it.  

To test the API functionality of the of the app, request_mock was used to mock the response from random.randint() to assert specific values in order to test the response of the app if it received said values.   

 

  

![jenkins build](https://github.com/gbarnacle79/week_6_project/blob/main/Images/jenkins_build.png) 

  

![coverage report](https://github.com/gbarnacle79/week_6_project/blob/main/Images/Coverage_report.png) 

  

  

## Risk Assessment: 

  

A risk assessment was performed to gauge potential issues the app may suffer from when running and to try avoid them. 

![Risk Assessment](https://github.com/gbarnacle79/week_6_project/blob/main/Images/riskassessment.png) 

  

## Changes Made:  

  

In the initial outline of the project, it was intended for the database to be hosted on GCP and to be a full MySQL database, this would allow for data to be saved for future viewings. This was changed to a simpler SQLite database it was easier to configure in regards to docker containers and accrued less cost on the Google Cloud Platform. In future iterations of this project this would be changed 

  

  

  

  

  

 

  

 
