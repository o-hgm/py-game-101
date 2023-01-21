#!/usr/bin/env python

import game_module.setup


if __name__ == "__main__":
    game_instance = game_module.setup.create_game_window()
    game_module.setup.run_event_loop()