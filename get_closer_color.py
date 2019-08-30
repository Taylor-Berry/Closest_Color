import numpy as np

chosen_pixel = [127, 255, 0]
available_pixels = {'red':[255,0,0], 'green':[0,255,0], 'blue':[0,0,255], 'magenta':[255,0,255],
                    'tomato':[255, 99, 71], 'lawn green':[124,252,0], 'steel blue':[70,130,180]}
distances = []

for key, value in available_pixels.items():
    a1 = np.asarray(value)
    c1 = np.asarray(chosen_pixel)
    curr_dist = np.linalg.norm(a1 - c1)
    distances += [curr_dist]
    if(curr_dist == min(distances)):
        curr_key = key

print(curr_key)
