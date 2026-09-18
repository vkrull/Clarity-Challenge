# Clarity-Challenge
This is me navigating the Clarity Challenge repository (for the original repo, see https://github.com/claritychallenge) to learn how the tools work, using `macOS` and VSCode.

## CEC1 Challenge
The CEC1 challenge is about building hearing aid algorithms to improve speech in noise for hearing aid users. For a brief description of the scenario and the challenge, see this [site](https://www.isca-archive.org/interspeech_2021/graetzer21_interspeech.html).

The [baseline system](https://claritychallenge.org/clarity_CEC1_doc/docs/cec1_baseline) includes sample data (rooms, scenes, listeners, and listeners assigned to specific scenes) and walks you through accessing and utilizing the data.

## CEC2 Challenge

The CEC2 challenge is about improve speech understanding in noise when there is a single target speaker in background noise in a simulated living room scenario using a range of signal-to-noise ratios.

The baseline system includes NAL-R amplification and a compressor, both of which are set to some basic parameters in the `config.yaml` file. There is no front-end noise cancellation. Processed signals are evaluated with the HASPI metric. The challenge also used a panel of hearing impaired users to assess speech intelligibility.
