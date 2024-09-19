package com.chatapp;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;
import com.google.gson.Gson;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@WebServlet("/messages")
/**
 * MessageServlet handles sending and retrieving messages for the chat application.
 */
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
      try (PrintWriter out = response.getWriter()) {
        out.println("Message received: " + messageText);
      }
    } else {
      response.sendError(HttpServletResponse.SC_BAD_REQUEST, "Message is empty");
    }
  }

  @Override
  protected void doGet(HttpServletRequest request, HttpServletResponse response)
      throws ServletException, IOException {

    String path = request.getPathInfo();

    if ("/count".equals(path)) {
      // Handle the count request
      synchronized (messages) {
        int messageCount = messages.size();
        response.setContentType("application/json");
        try (PrintWriter out = response.getWriter()) {
          out.println("{ \"messageCount\": " + messageCount + " }");
        }
      }
    } else {
      // Handle the retrieval of messages
      synchronized (messages) {
        response.setContentType("application/json");
        Gson gson = new Gson();
        try (PrintWriter out = response.getWriter()) {
          out.println(gson.toJson(new MessageList(messages)));
        }
      }
    }
  }

  private static class Message {
    private final String text;
    private final long timestamp;

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

  /**
   * MessageList contains all messages for the chat application.
   */

  private static class MessageList {
    private final List<Message> messages;

    MessageList(List<Message> messages) {
      this.messages = messages;
    }

    public List<Message> getMessages() {
      return messages;
    }
  }
}
