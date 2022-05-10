## Exercise A
# 1. Load pandas and psychopy
import pandas as pd
from psychopy import core, sound, visual, event
import numpy as np

# 2. Load the picture verification simuli file
#    (look up the .read_csv method of pandas)
stimuli = pd.read_csv('picture_verification_stimuli.csv')

# 5. Loop over the item paths, and use them to create image stimuli;
#     display each image for 1 second.
window = visual.Window()
clock = core.Clock()
images = []
for item_path in stimuli['image_file']:
    image_stim = visual.ImageStim(window, image=item_path)
    images.append(image_stim)

images = np.random.permutation(images)
# from random import shuffle
# shuffle(images)
results = []
for image in images:
    image.draw()
    window.flip()
    # clock.reset()
    start_time = clock.getTime()
    keys = event.waitKeys(maxWait=5, keyList=['z', 'm'], timeStamped=clock, clearEvents=True)
    if keys is not None:
        key, end_time = keys[0]
    else:
        key = None
        end_time = clock.getTime()
    
    results.append({
        'start_time': start_time,
        'end_time': end_time,
        'key': key
    })

results = pd.DataFrame(results)
results['reaction_time'] = results['end_time'] - results['start_time']
results.to_csv('demo_output.csv')
