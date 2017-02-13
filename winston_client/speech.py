import hashlib
from os import system, path

class Speech(object):
    def __init__(self):
        self.file_path = path.dirname(path.realpath(__file__)) + "/static/"

    def hash_file(self, text):
        return hashlib.sha224(text).hexdigest() + ".mp3"

    def exists(self, filename):
        return path.isfile(self.file_path + filename)

    def make(self, text, text_type="ssml"):
        fn = self.hash_file(text)
        if self.exists(fn):
            return fn

        system('aws polly synthesize-speech --text-type %s --text "%s" --output-format mp3 --voice-id Joanna %s' % (
            text_type,
            text,
            self.file_path+fn
        ))
        return fn

    def chime(self):
        system("mplayer -ao alsa -really-quiet -noconsolecontrols %schime.mp3" % (self.file_path))

    def say(self, text):
        fn = self.make(text)
        system("mplayer -ao alsa -really-quiet -noconsolecontrols %s%s" % (self.file_path, fn))

