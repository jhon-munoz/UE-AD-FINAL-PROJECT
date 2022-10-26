import * as express from "express"
import * as UserController from "./userController"
import { User } from './model'

export const register = ( app: express.Application ) => {
    app.get('/', (req, res) => res.send('Hello World!'));

    app.get('/user', (req, res) => {
        res.status(200).json(UserController.listUsers())
    })

    app.post('/user', (req, res) => {
        const newUser: User = req.body
        res.status(200).json(UserController.addUser(newUser))
    })

    app.get('/user/:id', (req, res) => {
        const userId: number = parseFloat(req.params.id)
        res.status(200).json(UserController.findUser(userId))
    })

    app.put('/user', (req, res) => {
        const newUser: User = req.body
        res.status(200).json(UserController.updateUser(newUser))
    })

    app.delete('/user/:id', (req, res) => {
        const userId: number = parseFloat(req.params.id)
        res.status(200).json(UserController.deleteUser(userId))
    })

}
