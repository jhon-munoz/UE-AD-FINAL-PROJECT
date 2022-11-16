import jwt from 'jsonwebtoken';
import {TokenInput, User} from "./model";

export default class AuthService {

    authenticate(tokenIn: TokenInput) {
        let token = jwt.sign(tokenIn.username, tokenIn.password);
        console.log('Data', token)
        return `Token: ${token}`
    }

    userContext(token: string) {
        let data = jwt.decode(token)
        console.log('Data: ', data);
        return data
    }

}
