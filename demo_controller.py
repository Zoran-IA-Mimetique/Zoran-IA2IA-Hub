
import json
setpoint = 1.0
Kp, Ki, Kd = 0.8, 0.1, 0.05
x = 0.0; integral = 0.0; prev_error = 0.0
traj = []
for t in range(100):
    error = setpoint - x
    integral += error
    derivative = error - prev_error
    u = Kp*error + Ki*integral + Kd*derivative
    x += 0.1*u  # simple plant
    prev_error = error
    traj.append(round(x,4))
print(json.dumps({"setpoint":setpoint,"traj":traj[:10]+["..."],"final":round(x,4)}, indent=2))
