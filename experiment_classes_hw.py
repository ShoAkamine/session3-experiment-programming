from psychopy import core, visual, sound, event

class Experiment:
    def __init__(self, window_size, text_color, background_color):
        self.text_color = text_color
        self.window = visual.Window(window_size, color=background_color)
        self.fixation = visual.TextStim(self.window, '+', color=text_color)
        self.clock = core.Clock()
    
    def show_fixation(self, time=0.5):
        self.fixation.draw()
        self.window.flip()
        core.wait(time)

class Item:
    def __init__(self, experiment, name, cond, text, audio_path):
        self.experiment = experiment
        self.name = name
        self.cond = cond
        self.text = visual.TextStim(experiment.window, text=text, color=experiment.text_color)
        self.audio = sound.Sound(audio_path)

class Trial:
    def __init__(self, experiment, name, stimulus, message, cond, fixation_time=0.5, max_key_wait=5, keys=['z', 'm']):
        self.name = name
        self.experiment = experiment
        self.stimulus = stimulus
        self.message = message
        self.cond = cond
        self.fixation_time = fixation_time
        self.max_key_wait = max_key_wait
        self.keys = keys
    
    def run(self):
        self.stimulus.play()
        core.wait(1)

        self.experiment.show_fixation(self.fixation_time)

        self.message.draw()
        self.experiment.window.flip()
        
        start_time = self.experiment.clock.getTime()
        keys = event.waitKeys(maxWait=self.max_key_wait, keyList=self.keys, timeStamped=self.experiment.clock, clearEvents=True)
        if keys is not None:
            key, end_time = keys[0]
        else:
            key = None
            end_time = self.experiment.clock.getTime()
        
        self.experiment.window.flip()   #refresh the screen

        return {
            'trial': self.name,
            'cond': self.cond,
            'start_time': start_time,
            'end_time': end_time,
            'key': key
        }