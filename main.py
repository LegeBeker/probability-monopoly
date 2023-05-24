import barchart as bc
import monopoly as mp

data = mp.get_fields()
player_spot = 0

squares = list(data.keys())
values = list(data.values())

fig, ax = bc.bar_init(squares, values)

while True:
    mp.play_round(player_spot, data)
    bc.update_chart(squares, data, ax)
