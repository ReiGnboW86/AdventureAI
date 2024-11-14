import simpleaudio as sa

class SoundPlayer:
    def __init__(self):
        pass

    def play_sound(self, sound_file):
        wave_obj = sa.WaveObject.from_wave_file(sound_file)
        play_obj = wave_obj.play()
        play_obj.wait_done()

    def adjust_background_music(self, intensity):
        # Adjust background music based on intensity
        pass
