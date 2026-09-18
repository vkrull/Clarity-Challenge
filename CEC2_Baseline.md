# CEC2 Baseline
## Notes on how to code CEC2 Baseline 

# The Clarity Docs
Download the Clarity documentation at https://github.com/claritychallenge/clarity/blob/main/notebooks/02_Running_the_CEC2_baseline_from_commandline.ipynb

Save the Jupyter Notebook as a Python script and set `NBOOKROOT` to the root working directory (as I did not use the Jupyter notebook; this is a personal preference).

```Python
NBOOKROOT="/Users/rsx8867/Documents/Python/clarity"
```
The script calls for cloning the `Clarity` repository, but if you have already completed the CEC1 Baseline, then you can comment out that section.

The script consists of sections that are run on the Shell and other sections that run within the Python script, including Hydra (see documentation for details).
### Change the current working directory 
to the location of the shell scripts we wish to run
```Python
% cd /clarity/recipes/cec2/baseline     
```
### Inspect existing Configuration file

```Python
% cat config.yaml  
```
### Set the path.root and run the code as provided
```Python
% python enhance.py \                                                        
path.root=$NBOOKROOT \
path.metadata_dir="$\{path.root\}/clarity_data/demo/metadata" \
path.scenes_listeners_file="$\{path.metadata_dir\}/scenes_listeners.demo.json" \
path.listeners_file="$\{path.metadata_dir\}/listeners.json" \
path.scenes_folder="$\{path.root\}/clarity_data/demo/scenes"

```
### Remember to run script sections within the script
The enhanced audio (newly created folder: `baseline/exp/exp/enhanced_signals`) is available to play, but this works only for Jupyter notebooks.
```Python
from os import listdir
... from os.path import isfile, join
... 
... import IPython.display as ipd
... 
... audio_path="exp/exp/enhanced_signals"
... audio_files=[f for f in listdir(audio_path) if isfile(join(audio_path, f))]
... 
... file_to_play = join(audio_path, audio_files[0])
... print(file_to_play)
... ipd.Audio(file_to_play)

```

- The evaluation script generates the HASPI scores, which can then be plotted.
### Remember to save the plot
Do so before the `plt.show` command, or the interactive window remains open, and if you close it, then it resets the current figure instance (and the saved plot is blank). The plot is saved in the current working directory (`/clarity/recipes/cec2/baseline`).
```Python
plt.savefig('HASPI_Plot.png')
plt.show()
```

### Note:
It appears that variable names are switched, but the plot labels are also switched, so the plot shows the right data:

```Python

unprocessed_si = pd.read_csv("exp/exp/si.csv")
processed_si = pd.read_csv("exp/exp/si_unproc.csv")

data = np.array([processed_si.loc[:, "haspi"], unprocessed_si.loc[:, "haspi"]])

plt.boxplot(np.transpose(data))

plt.title("HASPI Scores")

plt.xticks([1, 2], ["Unprocessed", "Processed"])
```
