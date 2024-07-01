export default function AuthForm({ onSubmit, buttonText }) {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
  
    const handleSubmit = () => {
      onSubmit(username, password);
    };
  
    return (
      <div>
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
        <button onClick={handleSubmit}>{buttonText}</button>
      </div>
    );
  }
  