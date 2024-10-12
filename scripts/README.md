## Telegram Scraper
A Python script to scrape messages and images from Telegram channels using Telethon.

### Requirements
1. Python 3.x
2. Install dependencies:
```
pip install telethon python-dotenv asyncio
```
3. Create a .env file:
```
TG_API_ID=your_api_id
TG_API_HASH=your_api_hash
phone=your_phone_number
```
Get API_ID and API_HASH from my.telegram.org.

### Features
- **Scrape Messages**: Fetch up to message_limit messages from specified Telegram channels and save them as JSON.
- **Download Images**: Download images from specified channels and save them in an images/ directory.

### Usage
- Clone this repository and install dependencies.
- Add your API credentials to the .env file.
- Modify the message_channels and image_channels lists in the script as needed.
- Run the script:
```
python your_script.py
```

#### Output
- **Messages**: Saved as <channel_name>_messages.json.
- **Images**: Downloaded in the images/ directory.
#### Customization
- Edit the channel URLs in the script:
```
message_channels = ['https://t.me/DoctorsET', ...]
image_channels = ['https://t.me/lobelia4cosmetics', ...]
```