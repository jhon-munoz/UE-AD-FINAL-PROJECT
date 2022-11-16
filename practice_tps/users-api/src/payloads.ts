import { Length, IsDefined, IsEmail } from "class-validator";

export class UserPost {
  @IsDefined()
  @Length(2, 20)
  name: string;
  @IsDefined()
  @IsEmail()
  email: string;
  @IsDefined()
  @Length(4, 6)
  password: string;
  @IsDefined()
  role: string;
}
