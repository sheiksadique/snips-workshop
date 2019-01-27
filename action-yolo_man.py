#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from hermes_python.hermes import Hermes

INTENT_YOLO_MAN = "sheiksadique:yolo_man"


def main():
    with Hermes("localhost:1883") as h:
        h.subscribe_intent(INTENT_YOLO_MAN, how_are_you_callback).start()


def how_are_you_callback(hermes, intent_message):
    session_id = intent_message.session_id
    response = "Dude! Wassup"
    hermes.publish_end_session(session_id, response)


if __name__ == "__main__":
    main()
