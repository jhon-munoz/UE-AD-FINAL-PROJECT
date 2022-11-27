import { String, Literal, Record, Union } from "runtypes";
export const UserCreation = Record({
  name: String,
  email: String,
  password: String,
  role: Union(Literal("admin"), Literal("player"), Literal("reporter")),
});
export const UserLogin = Record({
  name: String,
  password: String,
});
