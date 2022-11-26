export interface User {
  name: string;
  email: string;
  role: "admin" | "player" | "reporter";
  badges: string[];
}
