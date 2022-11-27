import jwt from "jsonwebtoken";
import { TokenInput } from "./model";

export default class AuthService {
  authenticate(tokenIn: TokenInput) {
    return jwt.sign(tokenIn.username, tokenIn.password);
  }

  userContext(token: string) {
    return jwt.decode(token);
  }
}
