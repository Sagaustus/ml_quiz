import axios from 'axios';

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export const login = async (username, password) => {
  const response = await axios.post(`${API_URL}/token`, { username, password });
  localStorage.setItem('token', response.data.access_token); // Store token in localStorage
  return response.data;
};

export const register = async (user) => {
  const response = await axios.post(`${API_URL}/users/`, user);
  return response.data;
};

export const getUserProfile = async (token) => {
  const response = await axios.get(`${API_URL}/users/profile`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
  return response.data;
};

export const getQuizzes = async () => {
  const response = await axios.get(`${API_URL}/quizzes`);
  return response.data;
};

export const submitQuiz = async (token, quizData) => {
  const response = await axios.post(`${API_URL}/quizzes`, quizData, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
  return response.data;
};
