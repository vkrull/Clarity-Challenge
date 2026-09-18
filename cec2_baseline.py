# %% [markdown]
# # Using the Shell Interface
# 
# The tools and recipes included in the <a href = 'https://github.com/claritychallenge/clarity'>clarity challenge repository</a> have been designed so that they can be integrated into python scripts that entrants may use in order to generate custom datasets or to expand the default datasets using new audio or varying data creation parameters. However, for convenience, the baseline clarity tools can be accessed in the command line interface (CLI) via shell scripts. 
# 
# The python and shell scripts included in the repository make use of <a href='https://hydra.cc/'>Hydra</a> and <a href='https://hydra.cc/docs/plugins/submitit_launcher/'>Submitit</a>, two technologies which streamline the configuration and parallel operation of python code on both local and high performnce computing (HPC) environments.
# 
# The use of hydra for configuration allows for the existing shell scripts to be easily redirected to include new audio data and modify the various parameters of the data generation scripts such as output directory, interferer counts, HRTF dataset locations, target onset timing, head rotation parameters and more.

# %% [markdown]
# ## Setting the Location of the Project
# 
# For convenience, we are setting an environment variable with the location of the root working directory of the project. This variable wll be used in various places throughout the tutorial. Please change this value to reflect where you have installed this notebook on your system. 
# 

# %%

# %env NBOOKROOT=/

NBOOKROOT="/Users/rsx8867/Documents/Python/clarity"

# %% [markdown]
# ## Cloning the Clarity Repository
# We first need to install the Clarity package.

# %%
# import os
# import sys

# from IPython.display import clear_output

# print("Cloning git repo...")
# !git clone --quiet https://github.com/claritychallenge/clarity.git
# %cd clarity
# %pip install -e .

# sys.path.append(f'{os.getenv("NBOOKROOT")}/clarity')

# clear_output()
# print("Repository installed")

# %% [markdown]
# ## Install demo data
# 
# We will be using scene audio and associated metadata. These can be downloaded using the Clarity package's `demo_data` module.

# %%
# from clarity.data import demo_data

# %cd ../
# demo_data.get_metadata_demo()
# demo_data.get_scenes_demo()


# clear_output()
# print("Data installed")

# %% [markdown]
# ## Changing working Directory
# 
# Next, we change working directory to the location of the shell scripts we wish to run.

# %%
# %cd {os.environ['NBOOKROOT']}/clarity/recipes/cec2/baseline
# %pwd

# %% [markdown]
# ## Inspecting Existing Configuration
# 
# All of the included shell scripts take configurable variables from the yaml files in the same directory as the shell script.Typically these are named <code>config.yaml</code>, however, other names may be used if more than one shell script is in a directory.
# 
# We can inspect the contents of the config file using <code>!cat</code>:

# %%
# !cat config.yaml

# %% [markdown]
# The general organisation of the config files is hierarchical, with property labels depending on the script in question. The config file for the enhance and evaluate recipes contains configurable paramaters for both scripts. These include:
# - Paths for the locations of audio files, metadata and the export location for generated files
# - Paramaters for the NAL-R fitting
# - Paramaters for the automatic gain control (AGC) compressor used in the baseline enhancer
# - Parameters for the challenge evaluator
# - Parameters necessary for Hydra to run
# 
# The path.root parameter defaults to a null value (<code>???</code>) and must be overrided with a dataset root path when the python script is called in the command line.
# 
# e.g
# 
# ```
# user:~$ python mypythonscript.py path.root='/path/to/project' 
# ```
# 
# In this notebooke we will use the environment variable <code>$NBOOKROOT</code> which we defined at the start of the tutorial.
# 
# Note the lack of slash at the end of the <code>path.root</code> argument string. If you inspect a variable such as <code>path.metadata_dir</code> you will see that this slash is already included in the line.
# 
# ```
# path:
#   root: ???
#   metadata_dir: ${path.root}/clarity_data/metadata
# 
# ```

# %% [markdown]
# The general form for overriding a parameter in the CLI is dot indexed. For the following entry in a <code>config.yaml</code> file:
# ```
# A:
#   B:
#     parameter_0: some_value
#     parameter_1: some_other_value
# ```
# The CLI syntax to override those values would be:
# 
# ```
# User:~$ python myscript.py A.B.parameter_0="new_value" A.B.parameter_1="another_new_value"
# ```

# %% [markdown]
# ## Shell Scripts 
# 
# Typically, as stated above, all the work is done within python with configurable variables supplied by a <code>yaml</code> file which is parsed by Hydra inside the python code. 
# 
# The execution of this code is performed in the CLI and new configuration variable values are supplied as arguments to override defaults. 
# 

# %% [markdown]
# ---
# ### Additional steps for Colab Notebooks
# This version of this tutorial is designed to run on Google Colab. The editable installation of the clarity repository is by default not visible to the python interpreter in this environment, even though the installation cell above makes the clarity tools visible to the iPython interpreter. 
# 
# As such, we need to make sure that the standard python interpreter called in the shell magic that follows below has the location of the clarity packages in the PYTHONPATH variable.
# 
# For local environments, this step may not be necessary.

# %%
# %env PYTHONPATH=$PYTHONPATH:/content/clarity

# %% [markdown]
# ---
# We are now ready to run the prepared python script. However, the standard configuration is designed to work with the full clarity dataset. We can redirect the script to the correct folers by overriding the appropriate configuration parameters.

# %%
%%shell
python enhance.py \
path.root=$NBOOKROOT \
path.metadata_dir="$\{path.root\}/clarity_data/demo/metadata" \
path.scenes_listeners_file="$\{path.metadata_dir\}/scenes_listeners.demo.json" \
path.listeners_file="$\{path.metadata_dir\}/listeners.json" \
path.scenes_folder="$\{path.root\}/clarity_data/demo/scenes" 


# %% [markdown]
# Now we have the enhanced output. Below, we can load and play the audio to listen to examples of the results.

# %%
from os import listdir
from os.path import isfile, join

import IPython.display as ipd

audio_path="exp/exp/enhanced_signals"
audio_files=[f for f in listdir(audio_path) if isfile(join(audio_path, f))]

file_to_play = join(audio_path, audio_files[0])
print(file_to_play)
ipd.Audio(file_to_play)

# %% [markdown]
# Now we have enhanced audio we can use the evaluate recipe to generate HASPI scores for the signals. The evaluation is run in the same manner as the enhancement script.

# %%
%%shell
python evaluate.py \
path.root=$NBOOKROOT \
path.metadata_dir="$\{path.root\}/clarity_data/demo/metadata" \
path.scenes_listeners_file="$\{path.metadata_dir\}/scenes_listeners.demo.json" \
path.listeners_file="$\{path.metadata_dir\}/listeners.json" \
path.scenes_folder="$\{path.root\}/clarity_data/demo/scenes" 



# %% [markdown]
# Now the HASPI scores have been generated, it is possible to plot the results to assess the improvement imparted by the signal processing

# %%
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

unprocessed_si = pd.read_csv("exp/exp/si.csv")

processed_si = pd.read_csv("exp/exp/si_unproc.csv")

data = np.array([processed_si.loc[:, "haspi"], unprocessed_si.loc[:, "haspi"]])
plt.boxplot(np.transpose(data))
plt.title("HASPI Scores")
plt.xticks([1, 2], ["Unprocessed", "Processed"])

plt.savefig('HASPI_Plot.png')
plt.show()

# %% [markdown]
# We hope that this tutorial has been useful and has explained the process for using the recipe scripts using the Hydra configuration system. This approach can be applied to all of the CEC2 recipes that are included in the repository.


