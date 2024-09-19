# SimpleAnonymousChat


This is a simple anonymous chat application that allows users to send and view messages without the need for user accounts or logins. The application is built using Java Servlets, and it can be run on an Apache Tomcat server.

## Project Structure
### Main Servlet Code: MessageServlet.java
Located at src/main/java/com/chatapp/MessageServlet.java
This servlet handles sending and retrieving messages.
To run the servlet, you need to restart the server. You can do this by right-clicking on the server in your IDE and selecting "Restart". Make sure the Tomcat server is set up correctly in your IDE (e.g., Eclipse or VSCode) and running before interacting with the application.

### Dependencies: pom.xml

This file contains the dependencies for the project. You can install these dependencies using Maven with the following command:
#### mvn install

### Servlet Mapping Configuration: web.xml

This file defines the servlet mappings:

The MessageServlet is mapped to the /messages/* URL pattern, handling message-related operations.
The welcome-file element ensures that chatApp.html is loaded as the homepage when the server starts.
The servlet mapping section maps the URL /messages/* to the MessageServlet, so any requests made to this URL will be handled by that servlet.


### UI: chatApp.html
Located at src/main/webapp/chatApp.html, this HTML file represents the chat application's user interface:

Includes a text input for sending messages.
A button for retrieving the total message count.
A simple design to display messages in real-time using JavaScript polling

### Running the Project
Set up Tomcat Server
Ensure Apache Tomcat v10.1.26 is installed.
Set up Tomcat in your IDE (e.g., Eclipse or VSCode).
Deploy the project to the Tomcat server and start it.

### Start the Application
After deploying, navigate to the chat application's main page by visiting http://localhost:8080/ChatApplication/chatApp.html.
The homepage will automatically load, allowing you to interact with the chat.

### Running Tests
Run the test.py script to test the application's performance and recoverability. The script interacts with the /messages endpoint to POST and GET messages. Execute the script using:
#### python test.py
Ensure you have the required dependencies installed (e.g., requests, subprocess).

### Code Quality
#### Checkstyle
Code complexity can be checked using Checkstyle. Make sure you have the Checkstyle JAR (version 10.18.1) installed. Run the following command to check the code:
##### java -jar checkstyle-10.18.1-all.jar -c google_checks.xml src/main/java/com/chatapp


### Additional Notes
##### Install the latest Java JDK (version 22.0.1).
##### Install Apache Tomcat (version 10.1.26).
##### Install Apache Maven.
##### Install the Server Management Extension.
##### Configure Tomcat