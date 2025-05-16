from datetime import date
import pandas as pd
from mailer import Mailer
from dotenv import load_dotenv
import os
from pathlib import Path
import numpy as np

CURRENT_DIR = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
envars = CURRENT_DIR / ".env"
load_dotenv(envars)

# setup mail server/login
EMAIL_ADDRESS = os.getenv("AUTO_EMAIL")
EMAIL_PASSWORD = os.getenv("AUTO_PASSWORD")
PORT = 587  
EMAIL_SERVER = "smtp.gmail.com"

# setup mailer
MAILER = Mailer(EMAIL_SERVER, PORT, EMAIL_ADDRESS, EMAIL_PASSWORD)


def main():
    print("start program")
    
    MAILER.send_email(
        subject=f'This is a test emal',
        receiver=EMAIL_ADDRESS,
        name="John Doe",
    )

if __name__ == "__main__":
    main()
