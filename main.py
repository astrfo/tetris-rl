import gym_tetris
from gym_tetris.actions import MOVEMENT
from nes_py.wrappers import JoypadSpace


if __name__ == '__main__':
    env = gym_tetris.make('TetrisA-v0')
    env = JoypadSpace(env, MOVEMENT)

    env.reset()
    done = False
    while not done:
        state, reward, done, info = env.step(env.action_space.sample())
        env.render()
    env.close()