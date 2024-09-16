import mediainfo
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load sensitive information from environment variables
tracker_url = os.getenv("TRACKER_URL")
tmdb_api_key = os.getenv("TMDB_API_KEY")
yggtorrent_url = os.getenv("YGGTORRENT_URL")
yggtorrent_user = os.getenv("YGGTORRENT_USER")
yggtorrent_password = os.getenv("YGGTORRENT_PASSWORD")
seeding_folder = os.getenv("SEEDING_FOLDER")
torrent_folder = os.getenv("TORRENT_FOLDER")
nfo_folder = os.getenv("NFO_FOLDER")
root_path = os.getenv("ROOT_PATH")
tag = os.getenv("TAG", "ILT")  # Default to "ILT" if TAG is not set

# Ensure all required environment variables are set
required_vars = [
    "TRACKER_URL", "TMDB_API_KEY", "YGGTORRENT_URL", "YGGTORRENT_USER",
    "YGGTORRENT_PASSWORD", "SEEDING_FOLDER", "TORRENT_FOLDER", "NFO_FOLDER", "ROOT_PATH"
]

for var in required_vars:
    if not os.getenv(var):
        raise EnvironmentError(f"Environment variable {var} is not set")

# Load titles from JSON file
with open("titles.json", "r", encoding="utf-8") as json_file:
    data_titles = json.load(json_file)

# Call mediainfo.main with the loaded data
mediainfo.main(
    tracker_url, seeding_folder, torrent_folder, nfo_folder, tmdb_api_key,
    data_titles, yggtorrent_user, yggtorrent_password, yggtorrent_url, root_path, tag
)