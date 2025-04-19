import os
from datetime import datetime

import stripe
import json

# For Google Sheets - if needed later
# import gspread
# from oauth2client.service_account import ServiceAccountCredentials

def load_users_from_stripe():
    stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
    users = []

    subscriptions = stripe.Subscription.list(status="all", limit=100)
    for sub in subscriptions.auto_paging_iter():
        customer = stripe.Customer.retrieve(sub.customer)

        discord_id = customer.metadata.get("discord_id")  # required to store this
        expiry_date = datetime.fromtimestamp(sub.current_period_end).strftime('%Y-%m-%d')

        if discord_id:
            users.append({
                "discord_id": discord_id,
                "expiry_date": expiry_date
            })

    return users

def load_users_from_google_sheets():
    # Stub for now
    return [
        {"discord_id": "123456789012345678", "expiry_date": "2025-04-30"},
    ]

def load_users_from_postgresql():
    # Stub for now
    return [
        {"discord_id": "987654321098765432", "expiry_date": "2025-04-28"},
    ]

def load_users(source):
    if source == "stripe":
        return load_users_from_stripe()
    elif source == "google_sheets":
        return load_users_from_google_sheets()
    elif source == "postgresql":
        return load_users_from_postgresql()
    else:
        return []
