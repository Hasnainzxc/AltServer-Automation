# Alt Server Automation 🚀

## Overview

The Alt Server Automation script is designed to provide automated notifications via email when your Alt Server and PC are turned on. This script is a helpful tool to keep you informed and ensure that your Alt Server and PC are running smoothly. 📧💻

![Alt Server Automation](https://example.com/animation.gif)

## Getting Started 🛠️

### Prerequisites

Before using this script, you will need the following:

1. **Python**: Ensure you have Python installed on your PC. You can download it from [Python's official website](https://www.python.org/downloads/). 🐍

### How to Get Your Gmail SMTP Password 📬

To use this script for email notifications, you will need your Gmail SMTP password. Follow these steps to obtain it:

1. **Enable Less Secure Apps**: Log in to your Gmail account and go to [Less secure apps]([https://myaccount.google.com/lesssecureapps](https://myaccount.google.com/apppasswords)). Turn on "Allow less secure apps" to allow SMTP access. 🔒

2. **Generate an App Password**: Go to your Google Account's [Security page](https://myaccount.google.com/security) and under "App passwords," generate an app password specifically for this script. Save this password securely as it will be used in the script configuration. 🔑

### Configuration ⚙️

1. **Email to Receive Notifications**: Provide the email address where you want to receive Alt Server notifications. This can be set up in the script. 📩

2. **SMTP Email and Password**: In the script, replace the placeholders with your Gmail SMTP email address and the app password generated in the previous step. 💌

### Task Scheduler (Windows) 📅

To automate the script to run when your PC is turned on, follow these steps:

1. **Open Task Scheduler**: Search for "Task Scheduler" in the Windows Start menu and open it. 📆

2. **Create a New Task**: In Task Scheduler, create a new task and configure it as follows:
   - Name and describe the task.
   - Trigger: Select "When I log on" to run the task when you log in to your PC.
   - Action: Choose "Start a program" and browse to select the Python script.
   - Review and save your task. 🕒

Now, the script will automatically send email notifications when your Alt Server and PC are turned on. 🚀

## Usage 🚀

Once everything is set up, run the script to start monitoring your Alt Server and receive email notifications when it's running. 📧

## Contributing 🤝

Feel free to contribute to this project by opening issues or submitting pull requests. Your contributions are highly appreciated and will help improve this script for everyone. 🌟

## License 📜

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 📄
