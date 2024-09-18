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
