package com.vehicle.identifier.vicore.util;


import com.sun.mail.smtp.SMTPTransport;

import javax.activation.DataHandler;
import javax.activation.DataSource;
import javax.activation.FileDataSource;
import javax.mail.*;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeBodyPart;
import javax.mail.internet.MimeMessage;
import javax.mail.internet.MimeMultipart;
import java.io.File;
import java.io.UnsupportedEncodingException;
import java.util.Date;
import java.util.Properties;

public class EmailUtil {

//    private static final String SMTP_SERVER = "mail.gravityzero.co.zw";
//    private static final String USERNAME = "noreply@gravityzero.co.zw";
//    private static final String PASSWORD = "Gravity@123";
//    private static final String EMAIL_FROM = "noreply@gravityzero.co.zw";

    private static final String SMTP_SERVER = "smtp.gmail.com";
    private static final String USERNAME = "vimurungu@gmail.com";
    private static final String PASSWORD = "Windhawk1997";
    private static final String EMAIL_FROM = "vimurungu@gmail.com";

    private static final String EMAIL_TO_CC = "";

    public static void sendEmail(String toEmail, String subject, String body,
                                 String fileNameAndPath) throws UnsupportedEncodingException {


        //  toEmail = "claytonscm@gmail.com";
        Properties prop = System.getProperties();


       /* prop.put("mail.smtp.host", "mail.gravityzero.co.zw"); //optional, defined in SMTPTransport
        prop.put("mail.smtp.port", "26"); // default port 25
*/


        prop.put("mail.smtp.host", "smtp.gmail.com"); //optional, defined in SMTPTransport
        prop.put("mail.smtp.port", "587"); // default port 25



        prop.put("mail.smtp.auth", "true");
        prop.put("mail.smtp.starttls.enable", "true"); //enable STARTTLS


       /* prop.put("mail.smtp.starttls.enable", "true");
        prop.put("mail.smtp.port", "587");
        prop.put("mail.smtp.host", "smtp.office365.com");
        prop.put("mail.smtp.auth", "true");*/

        Session session = Session.getInstance(prop, null);
        Message msg = new MimeMessage(session);

        try {


            // from
            msg.setFrom(new InternetAddress(EMAIL_FROM, "Harare Institute Of Technology"));

            // to
            msg.setRecipients(Message.RecipientType.TO,
                    InternetAddress.parse(toEmail, false));

            // cc
            msg.setRecipients(Message.RecipientType.CC,
                    InternetAddress.parse(EMAIL_TO_CC, false));

            // subject
            msg.setSubject(subject);


            MimeMultipart multipart = new MimeMultipart("related");

            // first part (the html)
            BodyPart messageBodyPart = new MimeBodyPart();
            messageBodyPart.setContent("<html>" + body + "Thank you fo visiting.<br><br>" +

                    "<img src=\"cid:image\" />" +


                    "</html>", "text/html");
            multipart.addBodyPart(messageBodyPart);

            messageBodyPart = new MimeBodyPart();

            DataSource fds2 = null;
            if (System.getProperty("os.name").startsWith("Windows")) {

                fds2 = new FileDataSource(
                        "D:\\hit.png");
            } else {

                fds2 = new FileDataSource(
                        "/var/emailfooter.png");
            }

            messageBodyPart.setDataHandler(new DataHandler(fds2));
            messageBodyPart.setHeader("Content-ID", "<image>");
            multipart.addBodyPart(messageBodyPart);


            msg.setContent(multipart);


            if (fileNameAndPath != null) {
                File f = new File(fileNameAndPath);
                System.out.println(f.getName());
                BodyPart emailBody = new MimeBodyPart();
                emailBody.setText(body);
                MimeBodyPart attachment = new MimeBodyPart();
                DataSource source = new FileDataSource(fileNameAndPath);
                attachment.setDataHandler(new DataHandler(source));
                attachment.setFileName(f.getName());
                Multipart multipart2 = new MimeMultipart();
                multipart2.addBodyPart(attachment);
                multipart2.addBodyPart(emailBody);
                msg.setContent(multipart2);
            }

            msg.setSentDate(new Date());

            // Get SMTPTransport
            SMTPTransport t = (SMTPTransport) session.getTransport("smtp");
            System.out.println("Attempting connection");

            // connect
            t.connect(SMTP_SERVER, USERNAME, PASSWORD);
            System.out.println("Connected");

            // send
            t.sendMessage(msg, msg.getAllRecipients());

            System.out.println("Response: " + t.getLastServerResponse());

            t.close();

        } catch (MessagingException e) {
            e.printStackTrace();
        }

    }


    public static void managerEmail(String toEmail, String subject, String body,
                                    String fileNameAndPath) throws UnsupportedEncodingException {


        //  toEmail = "claytonscm@gmail.com";
        Properties prop = System.getProperties();


        prop.put("mail.smtp.host", "mail.gravityzero.co.zw"); //optional, defined in SMTPTransport
        prop.put("mail.smtp.port", "26"); // default port 25


        prop.put("mail.smtp.auth", "true");
        prop.put("mail.smtp.starttls.enable", "false"); //enable STARTTLS


       /* prop.put("mail.smtp.starttls.enable", "true");
        prop.put("mail.smtp.port", "587");
        prop.put("mail.smtp.host", "smtp.office365.com");
        prop.put("mail.smtp.auth", "true");*/

        Session session = Session.getInstance(prop, null);
        Message msg = new MimeMessage(session);

        try {


            // from
            msg.setFrom(new InternetAddress(EMAIL_FROM, "Sebastian Baumhoff"));

            // to
            msg.setRecipients(Message.RecipientType.TO,
                    InternetAddress.parse(toEmail, false));

            // cc
            msg.setRecipients(Message.RecipientType.CC,
                    InternetAddress.parse(EMAIL_TO_CC, false));

            // subject
            msg.setSubject(subject);

    /*        DataSource fds = new FileDataSource(
                    "D:\\ProjectX\\crm-backend\\src\\main\\resources\\emailfooter.jpg");
            msg.setDataHandler(new DataHandler(fds));
            msg.setHeader("Content-ID", "<image>");*/

            // content

            MimeMultipart multipart = new MimeMultipart("related");

            // first part (the html)
            BodyPart messageBodyPart = new MimeBodyPart();
            messageBodyPart.setContent("<html>" + body + "Sebastian Baumhoff<br>" +
                    "Marketing Manager<br>" +
                    "Autoworld Harare (PVT) Ltd<br>" +
                    "Cell:+263 (0) 779 899 080<br>" +
                    "Email:seb@autoworld.co.zw<br><br>" +

                    "24 Silwood Close, Chisipite Harare<br>" +
                    "Tel: +263 (0)867 700 4334 | Office Number: +263 (0)772 148 738<br><br>" +

                    "<img src=\"cid:image\" />" +


                    "</html>", "text/html");
            multipart.addBodyPart(messageBodyPart);

            messageBodyPart = new MimeBodyPart();

            DataSource fds2 = null;
            if (System.getProperty("os.name").startsWith("Windows")) {

                fds2 = new FileDataSource(
                        "D:\\ProjectX\\crm-backend\\src\\main\\resources\\emailfooter.png");
            } else {

                fds2 = new FileDataSource(
                        "/var/emailfooter.png");
            }

            messageBodyPart.setDataHandler(new DataHandler(fds2));
            messageBodyPart.setHeader("Content-ID", "<image>");
            multipart.addBodyPart(messageBodyPart);


            msg.setContent(multipart);


            if (fileNameAndPath != null) {
                File f = new File(fileNameAndPath);
                System.out.println(f.getName());
                BodyPart emailBody = new MimeBodyPart();
                emailBody.setText(body);
                MimeBodyPart attachment = new MimeBodyPart();
                DataSource source = new FileDataSource(fileNameAndPath);
                attachment.setDataHandler(new DataHandler(source));
                attachment.setFileName(f.getName());
                Multipart multipart2 = new MimeMultipart();
                multipart2.addBodyPart(attachment);
                multipart2.addBodyPart(emailBody);
                msg.setContent(multipart2);
            }

            msg.setSentDate(new Date());

            // Get SMTPTransport
            SMTPTransport t = (SMTPTransport) session.getTransport("smtp");
            System.out.println("Attempting connection");

            // connect
            t.connect(SMTP_SERVER, USERNAME, PASSWORD);
            System.out.println("Connected");

            // send
            t.sendMessage(msg, msg.getAllRecipients());

            System.out.println("Response: " + t.getLastServerResponse());

            t.close();

        } catch (MessagingException e) {
            e.printStackTrace();
        }

    }
}



