from .. import core


class GoogleSheetsClient:
    """Client for interacting with Google Sheets API."""

    def __init__(self, config: core.GoogleSheetsConfig | None = None) -> None:
        self.config = config or core.GoogleSheetsConfig()
