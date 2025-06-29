#!/usr/bin/env python3

import requests
from termcolor import colored
import sys
import os
import re

def banner():
    print(colored("╔═══════════════════════════════════════╗", "cyan", attrs=["bold"]))
    print(colored("║         🎯  KD TikTok Recon Tool      ║", "cyan", attrs=["bold"]))
    print(colored("╚═══════════════════════════════════════╝", "cyan", attrs=["bold"]))


def extract_username(input_value):
    match = re.search(r"(?:https?://)?(?:www\.)?tiktok\.com/@([a-zA-Z0-9._]+)", input_value)
    return match.group(1) if match else input_value


def fetch_tiktok_user(username):
    url = f"https://www.tiktok.com/node/share/user/@{username}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(colored("❌ Error fetching TikTok user. User may not exist or API blocked.", "red"))
            sys.exit(1)

        data = response.json()
        user = data["userInfo"]["user"]
        stats = data["userInfo"]["stats"]

        print(colored("\n🎵 TikTok Recon Report", "green", attrs=["bold"]))
        print(colored("=================================", "cyan"))
        print(f"👤 Username           : {user['uniqueId']}")
        print(f"📛 Nickname           : {user['nickname']}")
        print(f"📝 Bio                : {user.get('signature', 'N/A')}")
        print(f"✔️ Verified           : {'Yes' if user.get('verified', False) else 'No'}")
        print(f"📍 Followers          : {stats.get('followerCount', 0)}")
        print(f"🔄 Following          : {stats.get('followingCount', 0)}")
        print(f"❤️ Likes              : {stats.get('heartCount', 0)}")
        print(f"🎥 Videos             : {stats.get('videoCount', 0)}")
        print(f"🖼️ Profile Pic URL    : {user.get('avatarLarger')}")
        print(colored("=================================\n", "cyan"))

    except Exception as e:
        print(colored(f"❌ Error: {e}", "red"))
        sys.exit(1)


if __name__ == "__main__":
    os.system("clear")
    banner()

    if len(sys.argv) != 2:
        print(colored("Usage: python3 tiktok_recon.py <username_or_tiktok_profile_url>", "yellow"))
        sys.exit(1)

    input_value = sys.argv[1]
    username = extract_username(input_value)
    fetch_tiktok_user(username)
