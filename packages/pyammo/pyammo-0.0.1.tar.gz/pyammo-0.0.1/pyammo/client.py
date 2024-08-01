from typing import Union
import requests
import logging


class Client(object):
    """Client for interacting with the Artifacts MMO API."""

    def __init__(self, host: str = "https://api.artifactsmmo.com", token: str = None):
        """
        :param host: The host to connect to.
        :param token: The token to use for authentication.
        """
        self.host = host
        self.token = token

    def get_server_status(self) -> dict:
        """Get the server status."""
        try:
            response = requests.get(self.host)
            response.raise_for_status()
            return response.json()["data"]
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to get server status: {e}")
            return {
                "status": "error",
                "error": str(e),
            }

    def get_character_data(self, name: str) -> Union[dict, None]:
        """Get a character by name."""
        try:
            response = requests.get(f"{self.host}/characters/{name}")
            response.raise_for_status()
            return response.json()["data"]
        except requests.exceptions.RequestException as e:
            if response.status_code == 404:
                logging.error(f"Character '{name}' not found.")
                return None
            else:
                logging.error(f"Failed to get character '{name}' data: {e}")
                return None

    def move_character(self, name: str, x: int, y: int) -> dict:
        """Move a character to a new location."""
        try:
            response = requests.post(
                f"{self.host}/my/{name}/action/move",
                headers={"Authorization": f"Bearer {self.token}"},
                json={"x": x, "y": y},
            )
            response.raise_for_status()
            return response.json()["data"]
        except requests.exceptions.RequestException as e:
            if response.status_code == 404:
                logging.error(f"Map ({x}, {y}) not found.")
            elif response.status_code == 486:
                logging.error(
                    f"Character '{name}' is locked. Action is already in progress."
                )
            elif response.status_code == 490:
                logging.error(f"Character '{name}' already at destination ({x}, {y}).")
            elif response.status_code == 498:
                logging.error(f"Character '{name}' not found.")
            elif response.status_code == 499:
                logging.error(f"Character '{name}' in cooldown.")
            else:
                logging.error(f"Failed to move character '{name}' to ({x}, {y}): {e}")
                return None
