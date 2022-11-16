import { User } from "./model";
import { UserPost } from "./payloads";
import UserRepository from "./userRepository";

const userRepository = new UserRepository();

const listUsers = (): User[] => userRepository.getAllUsers();

const addUser = (user: UserPost): User => {
  const userId = userRepository.createUser(user.name);
  return userRepository.getUserById(userId);
};

const deleteUser = (userId: number): User => {
  const user = findUser(userId);
  if (user !== undefined) {
    userRepository.deleteUserById(userId);
    return user;
  }
};

const findUser = (userId: number): User => userRepository.getUserById(userId);

const updateUser = (userId: number, toUpdate: any): User => {
  let user = findUser(userId) as any;
  if (user !== undefined) {
    Object.keys(toUpdate)
      .filter((key) => Object.keys(user).includes(key))
      .every((key) => (user[key] = toUpdate[key]));
    userRepository.updateUser(user);
    return user as User;
  }
};

export { listUsers, addUser, deleteUser, findUser, updateUser };
