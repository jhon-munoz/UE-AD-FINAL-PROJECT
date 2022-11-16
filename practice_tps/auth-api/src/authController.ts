import {TokenInput, User} from './model'
import AuthService from './authService'

const authService = new AuthService()

const autheticate = (tokenIn: TokenInput) => {
    return authService.authenticate(tokenIn)
}

const userContext= (token: string) => {
    return authService.userContext(token)
}

export { autheticate, userContext }
