import { User, Admin, Player, Reporter } from "./model";
import UserRepository from "./userRepository";

const userRepository = new UserRepository();

const listUsers = (): User[] => userRepository.getAllUsers();

const addUser = (newUser: Omit<User, "id">): User => {
  const userId = userRepository.createUser(newUser.name);
  return userRepository.getUserById(userId);
};

const deleteUser = (userId: number): User => {
  const user = findUser(userId);
  userRepository.deleteUserById(userId);
  return user;
};

const findUser = (userId: number): User => userRepository.getUserById(userId);

const updateUser = (userId: number, toUpdate: any): User => {
  let user = findUser(userId) as any;
  Object.keys(toUpdate)
    .filter((key) => Object.keys(user).includes(key))
    .every((key) => (user[key] = toUpdate[key]));
  return user as User;
};

export { listUsers, addUser, deleteUser, findUser, updateUser };
