                                                                                                                                                                                                           # PersonalizedLearningPath.py
import random
from Subject import Subject

class PersonalizedLearningPath:
    def __init__(self):
        self.subjects = {
            'Algebra': Subject('Algebra'),
            'Geometry': Subject('Geometry'),
            'Trigonometry': Subject('Trigonometry'),
            'Calculus': Subject('Calculus')
        }
        self.user_performance = {subject: 0.5 for subject in self.subjects}

    def update_user_performance(self, subject, interaction_type):
        # Define weightage for different interaction types
        watched_video_weight = 0.1
        read_notes_weight = 0.05

        # Ensure the interaction type is valid
        if interaction_type not in ['watched_video', 'read_notes']:
            raise ValueError("Invalid interaction type. Please use 'watched_video' or 'read_notes'.")

        # Update user performance based on interaction type
        if interaction_type == 'watched_video':
            self.user_performance[subject] += watched_video_weight
        elif interaction_type == 'read_notes':
            self.user_performance[subject] += read_notes_weight

        # Ensure user performance stays within a valid range (0 to 1)
        self.user_performance[subject] = max(0, min(1, self.user_performance[subject]))

    def get_next_subject(self):
        return max(self.user_performance, key=self.user_performance.get)

    def get_next_topic(self):
        current_subject = self.get_next_subject()
        return self.subjects[current_subject].get_videos(), self.subjects[current_subject].get_notes()

# Example Usage
learning_path = PersonalizedLearningPath()

# Simulate user watching a video in Algebra
learning_path.update_user_performance('Algebra', 'watched_video')

# Get the next recommended topic based on updated user performance
videos, notes = learning_path.get_next_topic()

print(f"Based on updated user performance, the next recommended videos are: {videos}")
print(f"Based on updated user performance, the next recommended notes are: {notes}")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   