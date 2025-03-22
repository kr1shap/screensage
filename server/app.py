from flask import Flask, render_template, request, redirect, url_for, session
import cohere
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__, template_folder='templates')
app.secret_key = os.getenv('SECRET_KEY')  # Required for session management

# Initialize Cohere client with the API key from environment
cohere_api_key = os.getenv('COHERE_API_KEY')
if not cohere_api_key:
    raise ValueError("COHERE_API_KEY not found in environment variables. Please check your .env file or system environment.")

co = cohere.Client(cohere_api_key)

# Home Page Route
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        job_role = request.form.get('job_role')
        session['job_role'] = job_role  # Store job role in session

        # Generate AI questions for the quiz
        prompt = f"Generate 5 interview questions for a {job_role} role. Return them as a numbered list, one question per line:"
        response = co.generate(
            model='command',
            prompt=prompt,
            max_tokens=200
        )

        # Split into individual questions and remove intro line
        questions = response.generations[0].text.strip().split('\n')
        questions = [q.strip() for q in questions if q.strip() and not q.strip().startswith("Here are")]  # Filter out intro line
        questions = [q[2:] if len(q) > 2 else q for q in questions]

        #questions and reset sess data
        session['questions'] = questions
        session['current_question'] = 0  # Start with the first question
        session['answers'] = {}  # Initialize answers dictionary

        return redirect(url_for('quiz'))

    return render_template('home.html')

# Quiz Page Route
@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if 'questions' not in session:
        return redirect(url_for('home'))

    if request.method == 'POST':
        # Save the answer for the current question
        current_question_index = session['current_question']
        session['answers'][f'question{current_question_index + 1}'] = request.form.get('answer')

        # Move to the next question or submit if all questions are answered
        if 'next' in request.form:
            session['current_question'] += 1
        elif 'previous' in request.form:
            session['current_question'] -= 1
        elif 'submit' in request.form:
            # Send all answers to Cohere API for scoring and feedback
            prompt = (
                f"Job Role: {session['job_role']}\n"
                f"Answers: {session['answers']}\n"
                "Generate a score out of 100 and detailed feedback. "
                "Return the response in the following format:\n"
                "Score: [score]/100\n"
                "Feedback: [feedback]"
            )
            response = co.generate(
                model='command',
                prompt=prompt,
                max_tokens=300
            )

            # Parse the response to extract score and feedback
            result_text = response.generations[0].text
            score = "N/A"
            feedback = result_text  # Default to the entire response if parsing fails

            # Look for a score in the response (e.g., "Score: 85/100")
            if "Score:" in result_text and "Feedback:" in result_text:
                try:
                    # Extract the score (e.g., "85")
                    score_part = result_text.split("Score:")[1].strip()
                    score = score_part.split("/")[0].strip()

                    # Extract the feedback
                    feedback = result_text.split("Feedback:")[1].strip()
                except IndexError:
                    # If splitting fails, fall back to the entire response
                    feedback = result_text

            # Store score and feedback in session
            session['score'] = score
            session['feedback'] = feedback

            return redirect(url_for('results'))

    # Ensure current_question is within bounds
    session['current_question'] = max(0, min(session['current_question'], len(session['questions']) - 1))

    return render_template('quiz.html',
                           job_role=session['job_role'],
                           question=session['questions'][session['current_question']],
                           question_number=session['current_question'] + 1,
                           total_questions=len(session['questions']))
# Results Page Route
@app.route('/results')
def results():
    score = session.get('score', 'N/A')
    feedback = session.get('feedback', 'No feedback available.')
    return render_template('results.html', score=score, feedback=feedback)

if __name__ == '__main__':
    app.run(debug=True)