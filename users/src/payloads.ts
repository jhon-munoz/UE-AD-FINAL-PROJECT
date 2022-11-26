import { Length, IsEmail, IsAlphanumeric, IsIn } from "class-validator";

export class UserCreation {
  @IsAlphanumeric()
  @Length(2, 20)
  name: string;
  @IsEmail()
  email: string;
  @IsIn(["admin", "player", "reporter"])
  role: "admin" | "player" | "reporter";
}
