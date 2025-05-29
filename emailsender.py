import smtplib  # Import the module for sending emails using SMTP

# Prompting the user for sender email and password
fro = input("Enter the email of the sender: ")  # Sender's email address
pas = input("Enter the correct password of sender's email: ")  # Sender's email password (Use app password if using Gmail with 2FA)

# Prompting the user for recipient email and message content
to = input("Enter the email of the recipient: ")  # Recipient's email address
content = input("Enter the message for the mail: ")  # Message to be sent

# Function to send email
def sendEmail(to, content):
    try:
        # Connect to Gmail's SMTP server with TLS (Transport Layer Security)
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()  # Identify yourself to the server
        server.starttls()  # Upgrade the connection to a secure TLS/SSL connection

        # Login to the email account using the provided credentials
        server.login(fro, pas)

        # Send the email from sender to recipient
        server.sendmail(fro, to, content)

        print("Email sent successfully!")

    except Exception as e:
        print("Failed to send email. Error:", e)

    finally:
        # Always close the connection, even if an error occurred
        server.close()

# Call the function to send the email
sendEmail(to, content)
