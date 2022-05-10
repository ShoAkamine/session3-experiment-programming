# This is a compact version of the oop_experiment script.
# It uses some techniques that we have not covered in this course!
# If you don't understand what's going on, use the oop_experiment.py script instead ;)

from experiment_classes import Experiment, Item, Trial
import pandas as pd
import numpy as np

experiment = Experiment((800, 600), (-1, -1, -1), (1, 1, 1))

stimuli = pd.read_csv('picture_verification_stimuli.csv')
items = [Item(experiment, stimulus['item'], stimulus['image_file']) for index, stimulus in stimuli.iterrows()]
image_trials = [Trial(experiment, f'{item.name}_image', item.image) for item in items]
text_trials = [Trial(experiment, f'{item.name}_text', item.text) for item in items]

trials = np.random.permutation(image_trials + text_trials)
results = [trial.run() for trial in trials]

results = pd.DataFrame(results)
results['reaction_time'] = results['end_time'] - results['start_time']
results.to_csv('demo_output.csv')
