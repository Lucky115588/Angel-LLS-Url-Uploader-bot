#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Thank you @LazyDeveloperr 

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)


if __name__ == "__main__" :
    # create download directory, if not exist
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    plugins = dict(
        root="plugins"
    )
    app = pyrogram.Client(
        "BewafaAngelPriya",
        bot_token=Config.8720530225:AAFfBXw7LQeoDZKS7rQqFRevQh7boxV5wfQ,
        api_id=Config.27339028,
        api_hash=Config.c75a5ed5a4377ce65c947360d29ede05,
        plugins=plugins
    )
    Config.AUTH_USERS.add(7025126355)
    app.run()
