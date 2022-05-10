from experiment_classes import Experiment, Item, Trial
import pandas as pd
import numpy as np

experiment = Experiment((800, 600), (-1, -1, -1), (1, 1, 1))

experiment.show_fixation(2)

stimuli = pd.read_csv('picture_verification_stimuli.csv')
items = []
for index, stimulus in stimuli.iterrows():
    items.append(Item(experiment, stimulus['item'], stimulus['image_file']))

trials = []
for item in items:
    trials.append(Trial(experiment, f'{item.name}_image', item.image))
    trials.append(Trial(experiment, f'{item.name}_text', item.text))

trials = np.random.permutation(trials)
results = []
for trial in trials:
    results.append(trial.run())

results = pd.DataFrame(results)
results['reaction_time'] = results['end_time'] - results['start_time']
results.to_csv('demo_output.csv')
