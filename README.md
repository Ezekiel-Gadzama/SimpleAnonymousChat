# SimpleAnonymousChatApplicat


This is a simple anonymous chat application that allows users to send and view messages without the need for user accounts or logins. The application is built using Java Servlets, and it can be run on an Apache Tomcat server.

Project Structure
Main Servlet Code: MessageServlet.java

This servlet handles sending and retrieving messages.
To run the servlet, you need to restart the server. You can do this by right-clicking on the server in your IDE and selecting "Restart". Make sure the Tomcat server is set up correctly in your IDE (e.g., Eclipse or VSCode) and running before interacting with the application.
Dependencies: pom.xml

This file contains the dependencies for the project. You can install these dependencies using Maven with the following command:
### mvn install

### Servlet Mapping Configuration: web.xml

This file defines the servlet mappings. The MessageServlet is mapped to the /messages/* URL pattern. Here's a breakdown of the key parts:
The MessageServlet is responsible for handling message-related operations.
The welcome-file ensures that chatApp.html is loaded as the homepage when the server starts.
The servlet mapping section maps the URL /messages/* to the MessageServlet, meaning any requests made to this URL will be handled by that servlet.

## Test Script: test.py

This Python script tests the time behavior, recoverability, and code complexity of the chat application. To run the script, you can use the terminal with:
#### python test.py
Make sure you have the required dependencies installed (e.g., requests, subprocess).



## UI: chatApp.html
###### src/main/webapp/chatApp.html
This HTML file represents the chat application's user interface. It includes:
A text input for sending messages.
A button for retrieving the total message count.
A simple design to display messages in real-time using JavaScript polling.


## Running the Project
Set up Tomcat Server:

Ensure Apache Tomcat is installed and set up in your IDE (e.g., Eclipse or VSCode).
Deploy the project to the Tomcat server and start it.
Start the Application:

After deploying, navigate to the chat application's main page by visiting http://localhost:8080/ChatApplication/chatApp.html. The homepage will automatically load, allowing you to interact with the chat.
Running Tests:

You can run the test.py script to test the application's performance and recoverability. The script interacts with the /messages endpoint to POST and GET messages.
Checkstyle:

Code complexity can be checked using Checkstyle. Make sure you have the Checkstyle JAR installed, then run the following command to check the code:
##### java -jar checkstyle-10.18.1-all.jar -c google_checks.xml src/main/java/com/chatapp


