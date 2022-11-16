interface UserBase {
  user_id: number;
  name: string;
}

interface Admin extends UserBase {
  role: "admin";
}

interface Player extends UserBase {
  role: "player";
  badges: string[];
}

interface Reporter extends UserBase {
  role: "reporter";
}

type User = Admin | Player | Reporter;

export { User, Admin, Player, Reporter };
