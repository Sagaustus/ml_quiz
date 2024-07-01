'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';
import { register } from '../../utils/api';

export default function Register() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [email, setEmail] = useState('');
  const router = useRouter();

  const handleRegister = async () => {
    try {
      const response = await register({ username, password, email });
      console.log(response);
      router.push('/login');
    } catch (error) {
      console.error('Error registering', error);
    }
  };

  return (
    <div>
      <h1>Register</h1>
      <input
        type="text"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        placeholder="Username"
      />
      <input
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        placeholder="Password"
      />
      <input
        type="email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        placeholder="Email"
      />
      <button onClick={handleRegister}>Register</button>
    </div>
  );
}
