import * as express from "express";
import UserController from "./userController.js";
import { UserCreation, UserLogin } from "./payloads.js";

const controller = new UserController();

export const register = (app: express.Application) => {
  app.get("/", async (_req, res) => res.send("Hello World!"));

  app.post("/login", async (req, res) => {
    try {
      const userLogin = UserLogin.check(req.body);
      const token = await controller.getUserToken(userLogin);
      if (token !== "") res.status(200).send(token);
      res.status(422).send();
    } catch (err) {
      res.status(400).send(err.details);
    }
  });

  app.get("/users", async (req, res) => {
    if (req.query.token === undefined) {
      res.status(401).send();
      return;
    }
    const include_deleted =
      (await controller.getRoleFromToken(req.query.token.toString())) ===
        "admin" && Boolean(req.query.include_deleted);
    const users = await controller.getAllUsers(include_deleted);
    res.status(200).json(users);
  });

  app.get("/users/:name", async (req, res) => {
    const username = req.params.name;
    if (
      req.query.token === undefined ||
      ((await controller.getRoleFromToken(req.query.token.toString())) !==
        "admin" &&
        (await controller.getUsernameFromToken(req.query.token.toString())) !==
          username)
    ) {
      res.status(401).send();
      return;
    }
    const include_deleted =
      (await controller.getRoleFromToken(req.query.token.toString())) ===
        "admin" && Boolean(req.query.include_deleted);
    const user = await controller.getUserByName(username, include_deleted);
    if (user !== null) res.status(200).json(user);
    else res.status(404).send();
  });

  app.post("/users", async (req, res) => {
    try {
      const userCreation = UserCreation.check(req.body);
      const token = await controller.createUser(userCreation);
      if (token !== "") res.status(201).send(token);
      res.status(422).send();
    } catch (err) {
      res.status(400).send(err.details);
    }
  });

  app.delete("/users/:name", async (req, res) => {
    if (
      req.query.token === undefined ||
      (await controller.getRoleFromToken(req.query.token.toString())) !==
        "admin"
    ) {
      res.status(401).send();
      return;
    }
    const username = req.params.name;
    const user = await controller.getUserByName(username);
    if (user !== null) {
      await controller.deleteUserByName(username);
      res.status(200).json(user);
    } else res.status(404).send();
  });

  app.put("/users/:name", async (req, res) => {
    const username = req.params.name;
    if (
      req.query.token === undefined ||
      (await controller.getUsernameFromToken(req.query.token.toString())) !==
        username
    ) {
      res.status(401).send();
      return;
    }
    const toUpdate: any = {};
    if (req.body.email) toUpdate.email = req.body.email;
    if (req.body.role) toUpdate.role = req.body.role;
    if ((await controller.getUserByName(username)) === null)
      res.status(404).send();
    else {
      await controller.updateUser(username, toUpdate);
      res.status(202).json(await controller.getUserByName(username));
    }
  });
};
