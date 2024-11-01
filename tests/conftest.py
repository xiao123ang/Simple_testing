# tests/conftest.py
import pytest
import subprocess
import yagmail

def pytest_sessionfinish(session, exitstatus):
    """Hook to run after all tests are finished."""
    # Generate the Allure report
    subprocess.run(["allure", "generate", "./reports", "-o", "./reports/html", "--clean"], check=True)
    
    # Send email with the report
    send_email_report()

def send_email_report():
    # Email configuration
    receiver = "receiver@example.com"  # Replace with the actual receiver's email
    subject = "Automated Test Report"
    body = "Please find the attached test report."
    report_path = "./reports/html/index.html"  # Path to the Allure report

    # Initialize yagmail
    yag = yagmail.SMTP("your_email@example.com", "your_password")  # Replace with your email and password

    # Send the email
    yag.send(
        to=receiver,
        subject=subject,
        contents=body,
        attachments=report_path,
    )
    print("Email sent successfully.")