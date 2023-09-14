import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import random
import datetime
import requests

# Gmail account credentials
sender_email = "YOUR@gmail.com"
sender_password = "YOU PASSWORD"

# Recipient email addresses (add or remove as needed)

recipient_emails = [
    "c@icloud.com",
    "@yahoo.com",
]



# Email subject
subject = "PC Turned On"

# Generate a random message for variety
random_messages = [
    "Your ALR SERVER is up and running!",
    "Good news, your ALT SERVER is online!",
    "Time to get things done—your ALT SERVER is on!",
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

# Define the correct GIF URLs
gif_urls = [
    "https://media.giphy.com/media/MT5UUV1d4CXE2A37Dg/giphy.gif",
    "https://media.giphy.com/media/nGMnDqebzDcfm/giphy.gif",
    "https://media.giphy.com/media/3oKIPnAiaMCws8nOsE/giphy.gif",
    "https://media.giphy.com/media/mcsPU3SkKrYDdW3aAU/giphy.gif",
    "https://media.giphy.com/media/FoVzfcqCDSb7zCynOp/giphy.gif",
    "https://media.giphy.com/media/dZX3AduGrY3uJ7qCsx/giphy.gif",
    "https://media.giphy.com/media/xT8qBsOjMOcdeGJIU8/giphy.gif",
    "https://media.giphy.com/media/5ntdy5Ban1dIY/giphy.gif",
    "https://media.giphy.com/media/l4FGIp6PDxcuJbvdC/giphy.gif",
]

# Select a random GIF URL
random_gif_url = random.choice(gif_urls)

# Create a MIMEText object to represent the email
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = ", ".join(recipient_emails)  # Join the recipient emails with a comma and space
msg["Subject"] = subject

# Create an HTML message with the inline GIF
html_message = f"""\
<html>
  <body>
    <p>{body}</p>
    <img src="cid:altservergif" alt="ALT Server GIF">
  </body>
</html>
"""

# Attach the HTML message
msg.attach(MIMEText(html_message, "html"))

# Download the GIF and attach it as an inline image
with open("random.gif", "wb") as gif_file:
    gif_file.write(requests.get(random_gif_url).content)

gif = MIMEImage(open("random.gif", "rb").read(), name="altserver.gif")
gif.add_header("Content-ID", "<altservergif>")
msg.attach(gif)

# Send the email using Gmail's SMTP server
