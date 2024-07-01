export default function UserProfile({ user }) {
    return (
      <div>
        <h1>{user.username}</h1>
        <p>{user.email}</p>
        <p>{user.full_name}</p>
      </div>
    );
  }
  