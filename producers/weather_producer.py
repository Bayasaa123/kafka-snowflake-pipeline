import requests
import json
import time
from confluent_kafka import Producer
from dotenv import load_dotenv
import os

load_dotenv()

KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")