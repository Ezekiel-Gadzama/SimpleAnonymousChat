package com.chatapp;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;
import com.google.gson.Gson;

@WebServlet("/messages")
public class MessageServlet extends HttpServlet {

    private static final List<Message> messages = new ArrayList<>();

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        String messageText = request.getParameter("message");

        if (messageText != null && !messageText.trim().isEmpty()) {
            synchronized (messages) {
                Message message = new Message(messageText, System.currentTimeMillis());
                messages.add(message);
            }

            response.setContentType("text/plain");
            PrintWriter out = response.getWriter();
            out.println("Message received: " + messageText);
        } else {
            response.sendError(HttpServletResponse.SC_BAD_REQUEST, "Message is empty");
        }
    }

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        String path = request.getPathInfo();
        if (path != null && path.equals("/count")) {
            // Handle the count request
            synchronized (messages) {
                int messageCount = messages.size();
                response.setContentType("application/json");
                PrintWriter out = response.getWriter();
                out.println("{ \"messageCount\": " + messageCount + " }");
            }
        } else {
            // Handle the retrieval of messages
            synchronized (messages) {
                response.setContentType("application/json");
                PrintWriter out = response.getWriter();
                Gson gson = new Gson();
                out.println(gson.toJson(new MessageList(messages)));
            }
        }
    }

    private static class Message {
        private String text;
        private long timestamp;

        Message(String text, long timestamp) {
            this.text = text;
            this.timestamp = timestamp;
        }

        public String getText() {
            return text;
        }

        public long getTimestamp() {
            return timestamp; 
        }
    }

    private static class MessageList {
        private List<Message> messages;

        MessageList(List<Message> messages) {
            this.messages = messages;
        }

        public List<Message> getMessages() {
            return messages;
        }
    }
}
