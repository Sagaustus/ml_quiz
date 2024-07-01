'use client';

import { useState, useEffect } from 'react';
import { getQuizzes, submitQuiz } from '../../utils/api';

export default function Quizzes() {
  const [quizzes, setQuizzes] = useState([]);
  const [score, setScore] = useState(0);

  useEffect(() => {
    const fetchQuizzes = async () => {
      const response = await getQuizzes();
      setQuizzes(response);
    };
    fetchQuizzes();
  }, []);

  const handleSubmit = async () => {
    const token = localStorage.getItem('token'); // Assuming token is stored in localStorage
    const response = await submitQuiz(token, {
      user_id: 1, // Example user ID
      course_id: 1, // Example course ID
      score,
      recommended_topics: []
    });
    console.log(response);
  };

  return (
    <div>
      <h1>Quizzes</h1>
      <ul>
        {quizzes.map(quiz => (
          <li key={quiz.id}>{quiz.title}</li>
        ))}
      </ul>
      <button onClick={handleSubmit}>Submit Quiz</button>
    </div>
  );
}
