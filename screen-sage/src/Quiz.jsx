import { useState } from "react";

const Quiz = ({questions}) => { 
      // State to track the current question and answers
  const [currentQ, setCurrentQ] = useState(0);
  const [userAnswers, setUserAnswers] = useState({});
  const [quizComplete, setQuizComplete] = useState(false);

  const { question, correctAns } = questions[currentQ];

  // Handle answer change for the current question
  const handleAnswerChange = (e) => {
    setUserAnswers({
      ...userAnswers,
      [currentQ]: e.target.value, // Store the typed answer for the current question
    });
  };

  // Move to the next question
  const handleNextQuestion = () => {
    if (currentQ < questions.length - 1) {
      setCurrentQ(currentQ + 1);
    }
  };

  // Submit quiz and calculate score
  const handleSubmitQuiz = () => {
    setQuizComplete(true);
  };

  // Calculate score (correct answers)
  const calculateScore = () => {
    let score = 0;
    questions.forEach((q, index) => {
      if (userAnswers[index] && userAnswers[index].toLowerCase() === q.correctAns.toLowerCase()) {
        score += 1;
      }
    });
    return score;
  };

 return <div className ="quiz-cont">
    <div className="question-cnt">
        <span className="active-q-no">{currentQ+1}</span>
        <span className="total-q">/{questions.length}</span>
    </div>
    <h2 className="quest">{question}</h2>

    <div className="answer-input">
          <textarea
              type="text"
              placeholder="let's think about it...."
              value={userAnswers[currentQ] || ""}
              onChange={handleAnswerChange}
            />
          </div>

          <div className="navigation-buttons">
            {currentQ < questions.length - 1 ? (
              <button onClick={handleNextQuestion}>Next Question</button>
            ) : (
              <button onClick={handleSubmitQuiz}>Submit Quiz</button>
            )}
          </div>
    
 </div>;
}

export default Quiz; 