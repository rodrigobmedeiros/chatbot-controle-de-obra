from .. import core


class TwilioClient:
    """Client for interacting with Twilio API."""

    def __init__(self, config: core.TwilioConfig | None = None) -> None:
        self.config = config or core.TwilioConfig()
