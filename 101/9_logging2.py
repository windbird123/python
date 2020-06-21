#!/usr/bin/env python
# -*- coding: utf-8 -*-


import logging

from logging.config import fileConfig
fileConfig("9_logging2.conf")

logger = logging.getLogger("test")
logger.info("hello")
