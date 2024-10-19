from functools import partial

from draw import *

curr_state = {
	"bot_loc": CartVertex2D(9,-14), 
	"bot_pose": PolarVertex2D(0.5,130),
	"tag_loc": CartVertex2D(2,-1),
	"tag_pose": PolarVertex2D(0.3,90),
	"frame":0,
}

def strategy_simple(state):
	speed = state["bot_loc"].get_distance(state["tag_loc"]) / 10 +0.1
	angle = state["tag_loc"].asPolar().addVector(CartVertex2D(-state["bot_loc"].x, -state["bot_loc"].y)).asPolar().a
	rotation = state["bot_pose"].asPolar().r - state["tag_loc"].asPolar().r
	print(f" from {state['bot_loc'].asPolar()} to {state['tag_loc'].asPolar()} got angle {angle:.3f} rotation {rotation}") 
	return PolarVertex2D(speed, angle), rotation

ani = FuncAnimation(fig, partial(animate_holonomic, state=curr_state, strategy=strategy_simple), interval=300)

run()