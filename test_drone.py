import time
from gym_pybullet_drones.envs.HoverAviary import HoverAviary

env = HoverAviary(gui=True)
obs, info = env.reset()

try:
  for _ in range(300):
    action = env.action_space.sample()
    obs, reward, terminated, truncated, info = env.step(action)
    time.sleep(1.0 / 60.0)
    if terminated or truncated:
      obs, info = env.reset()
finally:
  env.close()
