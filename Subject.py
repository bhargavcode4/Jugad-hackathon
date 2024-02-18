# Subject.py

class Subject:
    def __init__(self, name):
        self.name = name
        self.videos = []
        self.notes = []

    def add_video(self, video):
        self.videos.append(video)

    def add_note(self, note):
        self.notes.append(note)

    def get_videos(self):
        return self.videos

    def get_notes(self):
        return self.notes
