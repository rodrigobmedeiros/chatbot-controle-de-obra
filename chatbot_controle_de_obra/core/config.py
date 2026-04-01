__all__ = (
    "GoogleSheetsConfig",
    "TwilioConfig",
)

import pydantic_settings


class Config(pydantic_settings.BaseSettings):
    """Base Config class for the application."""


class TwilioConfig(Config, env_prefix="TWILIO_"):
    """Configuration for Twilio integration."""


class GoogleSheetsConfig(Config, env_prefix="GOOGLE_SHEETS_"):
    """Configuration for Google Sheets integration."""
