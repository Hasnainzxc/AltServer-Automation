import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import datetime

# Gmail account credentials
sender_email = "analogue00420@gmail.com"
sender_password = "hrrgykvpwfbduexe"

# Recipient email address
recipient_email = "hasnainzxc@icloud.com"  # Replace with your recipient's email address

# Email subject
subject = "PC Turned On"

# Generate a random message for variety
random_messages = [
    "Your PC is up and running!",
    "Good news, your PC is online!",
    "Time to get things done—your PC is on!",
    "Your ALT SERVER is ready to roll!",
]

# Select a random message
body = random.choice(random_messages)

# Add the date and time information
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
body += f"\n\nDate and Time PC Was Turned On: {current_time}"

# Add a message about the PC being ready to roll with random emojis
emojis = ["😀", "🚀", "💻", "👍"]
random_emojis = random.choices(emojis, k=3)  # Select 3 random emojis
body += f"\n\nThe PC is ready to roll {', '.join(random_emojis)}"

# Add a link to a random online animation (replace with your own links)
animation_links = [
    "https://example.com/animation1.gif",
    "https://example.com/animation2.gif",
    "https://example.com/animation3.gif",
]

# Select a random animation link
random_animation_link = random.choice(animation_links)

# Add the animation link to the email message
body += f"\n\n[Click here to view a random animation]({random_animation_link})"

# Create a MIMEText object to represent the email
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = recipient_email
msg["Subject"] = subject
msg.attach(MIMEText(body, "markdown"))

# Send the email using Gmail's SMTP server
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, msg.as_string())
    server.quit()
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email. Error: {str(e)}")
