# These are some homework exercises to practice working 
#  with pandas and psychopy.

## Exercise A
# 1. Load pandas and psychopy
import pandas as pd
from psychopy import core, sound, visual

# 2. Load the picture verification simuli file
#    (look up the .read_csv method of pandas)
picture_verification_stimuli = pd.read_csv('picture_verification_stimuli.csv')

# 3. Loop over the item names, and print them on the screen
#    (you can loop over a single column just like a list!)
for item_name in picture_verification_stimuli['item']:
    print(item_name)

# 4. Now, change your code to show a text stimulus with each item name,
#     with a 1 second pause in between, instead of using print().
window = visual.Window()
text_stim = visual.TextStim(window)
for item_name in picture_verification_stimuli['item']:
    text_stim.text = item_name
    text_stim.draw()
    window.flip()
    core.wait(0.5)

# 5. Loop over the item paths, and use them to create image stimuli;
#     display each image for 1 second.
for item_path in picture_verification_stimuli['image_file']:
    image_stim = visual.ImageStim(window, image=item_path)
    image_stim.draw()
    window.flip()
    core.wait(0.5)


## Exercise B
# 1. Load the lexical decision stimuli file 
lexical_decision_stimuli = pd.read_csv('lexical_decision_stimuli.csv')

# 2. Select all the high frequency words (HF)
#    (you can do this using masks, just like how we selected a single row)
hf_words = lexical_decision_stimuli[lexical_decision_stimuli['freq_category'] == 'HF']

# 3. Loop over the words, and create a sound stimulus for each
#    (you can specify the relative path as f'sounds/HF/{sound_name}.wav')
# 4. Play the sounds one-by-one, making sure there is some time between them
for word in hf_words['word']:
    sound_stim = sound.Sound(f'sounds/HF/{word}.wav')
    sound_stim.play()
    core.wait(0.5)

## Bonus exercise
# 1. Try to load in the image and/or sound stimuli first, 
#     before showing/playing them. You can use a list, and the .append()
#     method, to build a list of stimuli, and then use another for loop
#     to show/play them one by one.
# 2. Before showing/playing, try to randomise the order of stimuli; 
#     Google how to randomise the order of a list!
from random import shuffle

trials = []
for item_path in picture_verification_stimuli['image_file']:
    trials.append(visual.ImageStim(window, image=item_path))

shuffle(trials)
for trial in trials:
    trial.draw()
    window.flip()
    core.wait(0.5)
