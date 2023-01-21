#!/usr/bin/env python

import game_module.game


if __name__ == "__main__":
    game_instance = game_module.game.create_game_instance()
    game_instance.initialize()
    game_instance.loop()