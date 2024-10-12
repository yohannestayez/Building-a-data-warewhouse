from telethon import TelegramClient
import csv
import json
import os
import asyncio
import logging
from datetime import datetime
from dotenv import load_dotenv

# Setup logging for better tracking of progress
logging.basicConfig(level=logging.INFO)

# Load environment variables
load_dotenv('.env')
api_id = os.getenv('TG_API_ID')
api_hash = os.getenv('TG_API_HASH')
phone = os.getenv('phone')

# Create a folder for storing images
if not os.path.exists('images'):
    os.makedirs('images')

# Initialize the Telegram Client
client = TelegramClient('session_name', api_id, api_hash)

# Function to scrape text messages from a Telegram channel
async def scrape_telegram_messages(channel_url, message_limit=2000):
    try:
        await client.start(phone)
        entity = await client.get_entity(channel_url)
        
        messages = []
        async for message in client.iter_messages(entity, limit=message_limit):
            messages.append({
                'date': message.date,
                'sender_id': message.sender_id,
                'content': message.message,
                'media': bool(message.media)
            })
            logging.info(f"Scraped message on {message.date} from {channel_url}")
        
        return messages
    except Exception as e:
        logging.error(f"Error while scraping messages from {channel_url}: {e}")
        return []

# Function to scrape images from a Telegram channel
async def scrape_telegram_images(channel_url, image_limit=1000):
    try:
        await client.start(phone)
        entity = await client.get_entity(channel_url)
        
        image_count = 0
        async for message in client.iter_messages(entity, limit=image_limit):
            if message.media:
                file_path = await message.download_media(file=f'images/{message.id}.jpg')
                logging.info(f"Downloaded image: {file_path}")
                image_count += 1
        
        return image_count
    except Exception as e:
        logging.error(f"Error while scraping images from {channel_url}: {e}")
        return 0

# Function to save data as a JSON file
def save_as_json(data, filename):
    def convert(obj):
        """Helper function to convert non-serializable objects."""
        if isinstance(obj, datetime):
            return obj.isoformat()  # Convert datetime to ISO format string
        raise TypeError(f"Type {type(obj)} not serializable")

    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4, default=convert)
        logging.info(f"Saved data to {filename}")
    except Exception as e:
        logging.error(f"Error while saving data to {filename}: {e}")

# Main function to scrape both messages and images from the channels
async def scrape_telegram_channels():
    # List of channels to scrape text messages from
    message_channels = [
        'https://t.me/DoctorsET',
        'https://t.me/CheMed123',
        'https://t.me/lobelia4cosmetics',
        'https://t.me/yetenaweg',
        'https://t.me/EAHCI'
    ]
    
    # List of channels to scrape images from
    image_channels = [
        'https://t.me/CheMed123',
        'https://t.me/lobelia4cosmetics'
    ]

    # Scrape text messages
    for channel in message_channels:
        messages = await scrape_telegram_messages(channel)
        save_as_json(messages, f'{channel.split("/")[-1]}_messages.json')

    # Scrape images
    for channel in image_channels:
        image_count = await scrape_telegram_images(channel)
        logging.info(f"Downloaded {image_count} images from {channel}")

# Run the scraping process
if __name__ == '__main__':
    with client:
        client.loop.run_until_complete(scrape_telegram_channels())
