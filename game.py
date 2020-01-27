import world
from player import Player


def play():
    world.load_tiles()
    player = Player()
    room = world.tile_exists(player.location_x, player.location_y)
    while player.is_alive() and not player.victory:
        room = world.tile_exists(player.location_x, player.location_y)
        room.modify_player(player)

        if player.is_alive() and not player.victory:
            print("#=============#\nChoose an action:\n")
            available_actions = room.available_actions()
            for action in available_actions:
                print(action)
            print("#=============#")
            action_input = input('Action: ')
            for action in available_actions:
                if action_input == action.hotkey:
                    player.do_action(action, **action.kwargs)
                    break


if __name__ == "__main__":
    play()
