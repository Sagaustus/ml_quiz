import Link from 'next/link';

export default function Home() {
  return (
    <div>
      <h1>Welcome to the Quiz App</h1>
      <nav>
        <ul>
          <li><Link href="/login">Login</Link></li>
          <li><Link href="/register">Register</Link></li>
          <li><Link href="/quizzes">Quizzes</Link></li>
          <li><Link href="/profile">Profile</Link></li>
        </ul>
      </nav>
    </div>
  );
}
