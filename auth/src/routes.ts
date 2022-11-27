import * as express from "express";
import AuthService from "./authService";
import { TokenInput } from "./model";

const service = new AuthService();

export const register = (app: express.Application) => {
  app.post("/authenticate", (req, res) => {
    const tokenIn: TokenInput = req.body;
    res.status(200).json({ token: service.authenticate(tokenIn) });
  });

  app.get("/user-context/:token", (req, res) => {
    const username: string = req.params.token;
    res.status(200).json({ username: service.userContext(username) });
  });
};
