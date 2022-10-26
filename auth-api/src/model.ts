type User = {
    username: string
    role: number,
}

type TokenInput = {
    username: string
    password: string
}

export { User, TokenInput }
