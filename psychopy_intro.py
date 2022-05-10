from psychopy import visual, sound, core  # We import 3 components from the psychopy package

## Usually, when writing psychopy experiments, you prepare all stimuli before
##  the start of the experiment code; this is to make sure that there are no
##  irregular / unplanned delays once the experiment has started, which may
##  interfere with results.

# For visual stimuli, we need to first create a window
window = visual.Window(size=(400, 400))

# Some examples of visual stimuli
message = visual.TextStim(window)
grating = visual.GratingStim(window, tex='sin', mask='gauss', sf=10, name='gabor')
image = visual.ImageStim(window, image='images/baby.png')

# Some examples of auditory stimuli
note_c = sound.Sound('C', secs=1.0)
note_g = sound.Sound('G', secs=1.0)
audio = sound.Sound('sounds/HF/baby.wav')


## This is where the actual experiment code starts

message.text = 'Hello'  # Change the message text to 'Hello'
message.draw()  # This draws the text to the screen buffer; it is not visible yet
window.flip()  # This 'flips' the screen buffer, so that it actually becomes visible!
note_c.play()  # Play the C note
core.wait(2.0)  # Wait for 2 seconds

message.text = 'World'
message.draw()
window.flip()  # Flipping gives you control over when exactly things appear on the screen
note_g.play()
core.wait(2.0)

grating.draw()  # Draw the Gabor grating
window.flip()
core.wait(2.0)

image.draw()  # Draw the loaded image
window.flip()
audio.play()  # Play the loaded sound
core.wait(2.0)
