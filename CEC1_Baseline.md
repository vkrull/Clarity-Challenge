# The Clarity Docs
Download the Clarity documentation at https://github.com/claritychallenge/clarity/blob/main/notebooks/01_Installing_clarity_tools_and_using_metadata.ipynb
Local PDF:
[[Clarity Tools and Metadata Docs.pdf]]
# Let's start at the beginning - with the CEC1 Baseline
 *Vijay helped immensely with this*
## Notes on how to code CEC1 Baseline 
### How to save plot image file
```python
import matplotlib as plt
plt.savefig('filename.png')
```
Remember, it saves the plot image in the 'clarity' folder.

### How to know if a library is actually being imported or not in VSCode
In VSCode, type 
```python
matplotlib.
```
In VSCode, something should pop up saying all the things you can put after `matplotlib.`

### Stop making CEC1 Baseline download the dataset files every time!!
In VSCode, ONLY comment out this code:
```python
demo_data.get_metadata_demo()

demo_data.get_metadata_demo()

demo_data.get_targets_demo()

demo_data.get_interferers_demo()

demo_data.get_rooms_demo()

demo_data.get_scenes_demo()
```
So it looks like:
```python
# demo_data.get_metadata_demo()

# demo_data.get_metadata_demo()

# demo_data.get_targets_demo()

# demo_data.get_interferers_demo()

# demo_data.get_rooms_demo()

# demo_data.get_scenes_demo()
```
Make sure not to remove this code,
```python
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
```
Because here it is actually reading the metadata/data from the JSON files.

# How to fix CEC1 Baseline problems
### How to fix folder path problems in the CEC1 Baseline

```python
import os 
import sys 
print("Changing directory...") 
%cd clarity 
print("Installing Clarity tools")
%pip install -e . 
sys.path.append(os.getcwd()) 
print("Moving back to project root directory") 
%cd ..
```
From the clarity docs, when you paste the code, change all the `%` to `os.` Because in IDLE Shell, this works in the code, but with VSCode it does not.

## Completely unnecessary code that Vidya added

```python
# This finds the exact folder where your script is saved

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_path(relative_path):

return os.path.join(BASE_DIR, relative_path)
```
