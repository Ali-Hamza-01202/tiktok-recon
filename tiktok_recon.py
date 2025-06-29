#!/usr/bin/env python3

from TikTokApi import TikTokApi
from termcolor import colored
import sys
import os
import re
import asyncio


def banner():
    print(colored("╔═══════════════════════════════════════╗", "cyan", attrs=["bold"]))
    print(colored("║        🎯  KD TikTok Recon Tool       ║", "cyan", attrs=["bold"]))
    print(colored("╚═══════════════════════════════════════╝", "cyan", attrs=["bold"]))


def extract_username(input_value):
    match = re.search(r"(?:https?://)?(?:www\.)?tiktok\.com/@([a-zA-Z0-9._]+)", input_value)
    return match.group(1) if match else input_value


async def fetch_tiktok_user(username):
    try:
        async with TikTokApi() as api:
            user = await api.user(username=username).info()

            user_data = user['user']
            stats = user['stats']

            print(colored("\n🎵 TikTok Recon Report", "green", attrs=["bold"]))
            print(colored("=================================", "cyan"))
            print(f"👤 Username           : {user_data.get('uniqueId')}")
            print(f"📛 Nickname           : {user_data.get('nickname')}")
            print(f"📝 Bio                : {user_data.get('signature', 'N/A')}")
            print(f"✔️ Verified           : {'Yes' if user_data.get('verified') else 'No'}")
            print(f"📍 Followers          : {stats.get('followerCount')}")
            print(f"🔄 Following          : {stats.get('followingCount')}")
            print(f"❤️ Likes              : {stats.get('heartCount')}")
            print(f"🎥 Videos             : {stats.get('videoCount')}")
            print(f"🖼️ Profile Pic URL    : {user_data.get('avatarLarger')}")
            print(colored("=================================\n", "cyan"))

    except Exception as e:
        print(colored(f"❌ Error: {e}", "red"))
        sys.exit(1)


if __name__ == "__main__":
    os.system("clear")
    banner()

    if len(sys.argv) != 2:
        print(colored("Usage: python3 tiktok_recon.py <username_or_profile_url>", "yellow"))
        sys.exit(1)

    input_value = sys.argv[1]
    username = extract_username(input_value)

    asyncio.run(fetch_tiktok_user(username))
