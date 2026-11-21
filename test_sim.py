import time
import pybullet as p
import pybullet_data

p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.81)

p.loadURDF("plane.urdf")
robot_id = p.loadURDF("husky/husky.urdf", [0.0, 0.0, 0.2])

for _ in range(240):
  p.resetBaseVelocity(
      robot_id, linearVelocity=[1.5, 0.0, 0.0], angularVelocity=[0.0, 0.0, 0.3]
  )
  p.stepSimulation()
  time.sleep(1.0 / 60.0)

p.disconnect()
