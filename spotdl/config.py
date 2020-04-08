import appdirs
import yaml
import os

import spotdl.util

DEFAULT_CONFIGURATION = {
    "spotify-downloader": {
        "no-remove-original": False,
        "manual": False,
        "no-metadata": False,
        "no-fallback-metadata": False,
        "avconv": False,
        "directory": spotdl.util.get_music_dir(),
        "overwrite": "prompt",
        "input-ext": ".m4a",
        "output-ext": ".mp3",
        "write-to": None,
        "trim-silence": False,
        "download-only-metadata": False,
        "dry-run": False,
        "music-videos-only": False,
        "no-spaces": False,
        "file-format": "{artist} - {track_name}",
        "search-format": "{artist} - {track_name} lyrics",
        "youtube-api-key": None,
        "skip": None,
        "write-successful": None,
        "log-level": "INFO",
        "spotify_client_id": "4fe3fecfe5334023a1472516cc99d805",
        "spotify_client_secret": "0f02b7c483c04257984695007a4a8d5c",
    }
}

default_config_file = os.path.join(
    appdirs.user_config_dir(),
    "spotdl",
    "config.yml"
)

def read_config(config_file):
    with open(config_file, "r") as ymlfile:
        config = yaml.safe_load(ymlfile)
    return config


def dump_config(config_file, config=DEFAULT_CONFIGURATION):
    with open(config_file, "w") as ymlfile:
        yaml.dump(DEFAULT_CONFIGURATION, ymlfile, default_flow_style=False)


def get_config(config_file):
    if os.path.isfile(config_file):
        config = read_config(config_file)
    else:
        config = DEFAULT_CONFIGURATION
        dump_config(config_file, config=DEFAULT_CONFIGURATION)

        # log.info("Writing default configuration to {0}:".format(config_file))

        # for line in yaml.dump(
        #     DEFAULT_CONFIGURATION["spotify-downloader"], default_flow_style=False
        # ).split("\n"):
        #     if line.strip():
        #         log.info(line.strip())
        # log.info(
        #     "Please note that command line arguments have higher priority "
        #     "than their equivalents in the configuration file"
        # )

    return config["spotify-downloader"]

