import json

configs = {
    "start": 0.0,
    "video_name": "2002.webm",
    "duration": 2.0,
}


with open("config.json", "w") as f:
    json.dump(configs, f, indent=4)
