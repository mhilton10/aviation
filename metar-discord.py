import requests
from bs4 import BeautifulSoup

def get_kccr_atis():
    # URL for the latest ATIS information at KCCR
    url = "https://aviationweather.gov/cgi-bin/data/metar.php?ids=KCCR&hours=0&order=id%2C-obs&sep=true"

    # Send an HTTP request to fetch the ATIS information
    response = requests.get(url)

    if response.status_code == 200:
        # Extract the text content of the METAR information
        atis_info = response.text.strip()
        return atis_info

        if atis_element:
            # Extract the text content of the ATIS element
            atis_info = atis_element.text.strip()
            return atis_info
        else:
            return "Unable to retrieve ATIS information."

    else:
        return f"Failed to fetch ATIS information. Status code: {response.status_code}"

def send_discord_webhook(content):
    # Replace 'YOUR_DISCORD_WEBHOOK_URL' with your actual Discord webhook URL
    webhook_url = 'https://discordapp.com/api/webhooks/1199221321582776422/My073CFFbvzYe3lxmvSk6ziAi7D0AJibgXl6npQmimT7vf29s99XQGpvOoYbBnuSnPwT'

    # Payload for the Discord webhook
    payload = {'content': content}

    # Send the payload to the Discord webhook
    response = requests.post(webhook_url, json=payload)

    if response.status_code != 204:
        print(f"Failed to send Discord webhook. Status code: {response.status_code}")
    else:
        print("Discord webhook sent successfully.")

def main():
    # Get the latest ATIS information
    atis_info = get_kccr_atis()

    # Send the ATIS information to the Discord webhook
    send_discord_webhook(atis_info)

if __name__ == "__main__":
    main()
