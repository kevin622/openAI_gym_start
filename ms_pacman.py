# This file doesn't work ㅠㅠ
# gym.error.UnregisteredEnv: No registered env with id: MsPacman-v0
import gym
env = gym.make('MsPacman-v0')
env.reset()
for _ in range(100):
    env.render()
    env.step(env.action_space.sample())
env.close()