#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from queue import Queue
from threading import Thread

from loguru import logger

queue = Queue(3)
consumer_count = 2


class SingletonPoisonPill(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingletonPoisonPill, cls).__new__(cls)
        return cls.instance


class Consumer(Thread):
    def run(self) -> None:
        while True:
            value = queue.get(True)
            if value == SingletonPoisonPill:
                logger.info("Recv poison pill, terminate")
                break

            logger.info(f"Consumer: {value}")
            time.sleep(0.5)


class Producer(Thread):
    def run(self) -> None:
        for i in range(10):
            queue.put(i)
            logger.info(f"Producer: {i}")
            # time.sleep(0.1)

        # poison pill
        for i in range(consumer_count):
            queue.put(SingletonPoisonPill)


if __name__ == '__main__':
    producers = [Producer()]
    consumers = [Consumer() for _ in range(consumer_count)]

    # starts producer
    for p in producers:
        p.start()

    # starts consumer
    for c in consumers:
        c.start()

    for p in producers:
        p.join()

    for c in consumers:
        c.join()

    print("------ Done")
