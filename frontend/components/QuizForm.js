export default function QuizForm({ questions, onSubmit }) {
    const [answers, setAnswers] = useState({});
  
    const handleChange = (questionId, answer) => {
      setAnswers({
        ...answers,
        [questionId]: answer,
      });
    };
  
    const handleSubmit = () => {
      onSubmit(answers);
    };
  
    return (
      <div>
        {questions.map((question) => (
          <div key={question.id}>
            <p>{question.question_text}</p>
            {question.choices.map((choice) => (
              <label key={choice}>
                <input
                  type="radio"
                  name={question.id}
                  value={choice}
                  onChange={() => handleChange(question.id, choice)}
                />
                {choice}
              </label>
            ))}
          </div>
        ))}
        <button onClick={handleSubmit}>Submit</button>
      </div>
    );
  }
  