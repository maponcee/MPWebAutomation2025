import os

from dotenv import load_dotenv

load_dotenv()

user_name = os.getenv("EMAIL")
password = os.getenv("PASSWORD")


BASE_URL = {
    "development": "https://ecommerce-playground.lambdatest.io/",
    "staging": "https://ecommerce-playground.lambdatest.io/",
    "production": "https://ecommerce-playground.lambdatest.io/"
}
