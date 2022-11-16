import * as express from "express"
import * as AuthController from "./authController"
import {TokenInput} from './model'

export const register = ( app: express.Application ) => {

    app.post('/authenticate', (req, res) => {
        const tokenIn: TokenInput = req.body
        res.status(200).json(AuthController.autheticate(tokenIn))
    })

    app.get('/user-context/:token', (req, res) => {
        const token: string = req.params.token
        res.status(200).json(AuthController.userContext(token))
    })
}
