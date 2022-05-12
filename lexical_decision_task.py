from experiment_classes_hw import Experiment, Item, Trial
import pandas as pd
import numpy as np
import datetime as dt

#                        window size, text color,  background color
experiment = Experiment((800, 600), (-1, -1, -1), (1, 1, 1))

experiment.show_fixation(1.0)

stimuli = pd.read_csv('lexical_decision_stimuli.csv')

#Counterblance the stimuli (1 set contains 1 LF, 1 HF, 2 NWs; 5 sets in total)
stimuli_lf = stimuli.head(5)
stimuli_hf = stimuli.iloc[50:55]
stimuli_nw = stimuli.iloc[100:110]
stimuli_reduced = pd.concat([stimuli_lf, stimuli_hf, stimuli_nw])

items = []
for index, stimulus in stimuli_reduced.iterrows():
    if stimulus['freq_category'] == 'none':
        folder_name = 'NW'
    else:
        folder_name = stimulus['freq_category']
    word = stimulus['word']
    audio_path = f"sounds/{folder_name}/{word}.wav"
    #            Item(experiment, name, text,                        audio_path)
    items.append(Item(experiment, word, "Word (z) or non-word (m)?", audio_path))

trials = []
for item in items:
    #                   experiment, name,                 stimulus, message,    fixation_time=0.5, max_key_wait=5, keys=['z', 'm']
    trials.append(Trial(experiment, item.name, item.audio, item.text))

trials = np.random.permutation(trials)
results = []
for trial in trials:
    results.append(trial.run())

results = pd.DataFrame(results)
results['reaction_time'] = results['end_time'] - results['start_time']
now = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
results.to_csv(f'demo_output_{now}.csv')
