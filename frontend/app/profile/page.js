'use client';

import { useEffect, useState } from 'react';
import { getUserProfile } from '../../utils/api';

export default function Profile() {
  const [profile, setProfile] = useState(null);

  useEffect(() => {
    const fetchProfile = async () => {
      const token = localStorage.getItem('token'); // Assuming token is stored in localStorage
      const response = await getUserProfile(token);
      setProfile(response);
    };

    fetchProfile();
  }, []);

  if (!profile) return <div>Loading...</div>;

  return (
    <div>
      <h1>Profile</h1>
      <p>Username: {profile.username}</p>
      <p>Email: {profile.email}</p>
      <p>Full Name: {profile.full_name}</p>
    </div>
  );
}
