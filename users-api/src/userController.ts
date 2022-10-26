import { User } from './model'
import UserRepository from './userRepository'

/*const typedUsers: User[] = []

const listUsers = () => typedUsers

const addUser = (newUser: User) => {
    typedUsers.push(newUser)
    return typedUsers
}*/

// TODO: implement and export
// function findUser (userId: number): User { //@todo }

const userRepository = new UserRepository()

const listUsers = () => {
    return userRepository.getAllUsers()
}

const findUser= (userId: number) => {
    return userRepository.getUserById(userId)
}

const addUser = (newUser: User) => {
    userRepository.createUser(newUser.name)
    return userRepository.getAllUsers()
}

const updateUser = (newUser: User) => {
    userRepository.updateUser(
        newUser.id, newUser.name, newUser.score
    )
    return userRepository.getUserById(newUser.id)
}

const deleteUser= (userId: number) => {
    return userRepository.deleteUser(userId)
}


export { listUsers, addUser, findUser, updateUser, deleteUser }
