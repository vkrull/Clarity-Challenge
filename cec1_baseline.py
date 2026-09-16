import os
import sys

# This finds the exact folder where your script is saved
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_path(relative_path):
    return os.path.join(BASE_DIR, relative_path)

print("Changing directory...")
os.chdir(get_path("clarity"))
print("Installing Clarity tools")
os.system("pip install -e .")

sys.path.append(os.getcwd())
print("Moving back to project root directory")
os.chdir

## For this demonstration we will just download and install just the metadata dataset.
from clarity.data import demo_data

# demo_data.get_metadata_demo()
# demo_data.get_metadata_demo()
# demo_data.get_targets_demo()
# demo_data.get_interferers_demo()
# demo_data.get_rooms_demo()
# demo_data.get_scenes_demo()

# Reading the metadata files:
import json

with open("clarity_data/demo/metadata/scenes.demo.json") as f:
    scenes = json.load(f)

with open("clarity_data/demo/metadata/listeners.json") as f:
    listeners = json.load(f)

with open("clarity_data/demo/metadata/rooms.demo.json") as f:
    rooms = json.load(f)

with open("clarity_data/demo/metadata/listeners.json") as f:
    listeners = json.load(f)

with open("clarity_data/demo/metadata/scenes_listeners.dev.json") as f:
    scenes_listeners = json.load(f)

# Working with the metadata

scene_0 = scenes[0]
print(scene_0.keys())

print(scene_0["SNR"])
print(scene_0["listener"])
print(scene_0["duration"])

# processing a collection of scenes

import numpy as np
import matplotlib.pyplot as plt 

fig, ax = plt.subplots(1, 2)

# Get list of SNRs of scenes
snr_values = np.array([s["SNR"] for s in scenes], dtype="float32")

# Plot histogram
ax[0].hist(snr_values)
ax[0].set_title("Histogram of SNR values")
ax[0].set_xlabel("SNR (dB)")

# Get list of number of interferers in scenes
n_interferers = np.array([len(s["interferers"]) for s in scenes], dtype="int32")

# Prepare data for boxplot
snr_comparison_data = [
    [s for s, n in zip(snr_values, n_interferers, strict=True) if n == 2],
    [s for s, n in zip(snr_values, n_interferers, strict=True) if n == 3],
]

# Plot boxplot
ax[1].boxplot(np.array(snr_comparison_data, dtype="object"))
ax[1].set_xlabel("Number of interferers")
ax[1].set_ylabel("SNR (dB)")

plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.4, hspace=0.4)

# Save plot 1 
plt.savefig('Plot1.png')


fig.show()

room_id = scene_0["room"]

# Iterate through rooms to find the one named `room_id`

room = next((item for item in rooms if item["name"] == room_id), None)

print(room["dimensions"])



room_dict = {room["name"]: room for room in rooms}



room_id = scene_0["room"]
room_dict[room_id]
print(room["dimensions"])

#  Locating information about the scene's listener

scene_no = 32  # this is just an arbitrary index. try any from 0 - 49

scene = scenes[scene_no]

room = room_dict[scene["room"]]
current_listeners = scenes_listeners[scene["scene"]]


print(
    f"\nScene number {scene_no} "
    f'(ID {scene["scene"]}) has room dimensions of {room["dimensions"]}'
)

print(
    f"\nSimulated listeners for scene {scene_no} "
    f'have spatial attributes: \n{room["listener"]}'
)

print(f'\nAudiograms for listeners in Scene ID {scene["scene"]}')


fig, ax = plt.subplots(1, len(current_listeners))

ax[0].set_ylabel("Hearing level (dB)")
for i, curr_listener in enumerate(current_listeners):
    listener_data = listeners[curr_listener]
    (left_ag,) = ax[i].plot(
        listener_data["audiogram_cfs"],
        -np.array(listener_data["audiogram_levels_l"]),
        label="left audiogram",
    )
    (right_ag,) = ax[i].plot(
        listener_data["audiogram_cfs"],
        -np.array(listener_data["audiogram_levels_r"]),
        label="right audiogram",
    )
    ax[i].set_title(f"Listener {curr_listener}")
    ax[i].set_xlabel("Hz")
    ax[i].set_ylim([-100, 10])

plt.legend(handles=[left_ag, right_ag])
plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.4, hspace=0.4)

plt.savefig('Plot2.png')