# SmartNqData/smart_nq_realtime.py

import pika
import time
import json
import pandas as pd
from datetime import datetime

class SmartNqRealtime:
    def __init__(self, url, user, password):
        self.url = url
        self.user = user
        self.password = password
        self.connection = None
        self.channel = None
        self.retry_delay = 5  # seconds

    def connect(self):
        while True:
            try:
                parameters = pika.ConnectionParameters(
                    self.url,
                    5672,
                    '/',
                    pika.PlainCredentials(self.user, self.password)
                )
                self.connection = pika.BlockingConnection(parameters)
                self.channel = self.connection.channel()
                break
            except Exception as e:
                print(f"Connection failed: {e}. Retrying in {self.retry_delay} seconds...")
                time.sleep(self.retry_delay)

    def subscribe(self, queue_name, contract_symbol, callback):
        self.connect()
        
        # Declare the queue and bind it to all fanout exchanges
        self.channel.queue_declare(queue=queue_name, durable=True)
        
        def on_message(ch, method, properties, body):
            message = json.loads(body)
            if message['ContractSymbol'] == contract_symbol:
                df = self._parse_message(message)
                callback(df)

        self.channel.basic_consume(queue=queue_name, on_message_callback=on_message, auto_ack=True)

        print(f"Subscribed to queue {queue_name} for contract symbol {contract_symbol}. Waiting for messages...")
        self.channel.start_consuming()

    def _parse_message(self, message):
        # Flatten indicators
        indicators = json.loads(message['Indicators'])
        flat_indicators = {k: v for k, v in indicators.items()}

        # Map fields
        data = {
            'datetime': datetime.fromisoformat(message['Timestamp']),
            'open': message['Open'],
            'high': message['High'],
            'low': message['Low'],
            'close': message['Close'],
            'volume': message['Volume']
        }
        data.update(flat_indicators)

        # Convert to DataFrame
        df = pd.DataFrame([data])

        return df
