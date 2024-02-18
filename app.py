from flask import Flask, render_template, request
from PersonalizedLearningPath import PersonalizedLearningPath

app = Flask(__name__)
learning_path = PersonalizedLearningPath()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update_performance', methods=['POST'])
def update_performance():
    subject = request.form['subject']
    interaction_type = request.form['interaction_type']
    
    # Simulate user interaction
    learning_path.update_user_performance(subject, interaction_type)

    # Get the next recommended topic based on updated user performance
    videos, notes = learning_path.get_next_topic()

    return render_template('index.html', videos=videos, notes=notes)

if __name__ == '__main__':
    app.run(debug=True)
