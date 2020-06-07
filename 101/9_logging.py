#!/usr/bin/env python
# -*- coding: utf-8 -*-


import logging
if __name__ == '__main__':
    logger = logging.getLogger("my_logger")
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    logger.info("info")
    logger.warning("warning")
    logger.error("error")

    try:
        raise Exception("my exception")
    except Exception as e:
        logger.exception(e)
