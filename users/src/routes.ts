import * as express from "express";
import UserController from "./userController";
import { UserCreation } from "./payloads";
import { validate } from "class-validator";
import { plainToClass } from "class-transformer";

const controller = new UserController();

export const register = (app: express.Application) => {
  app.get("/", async (_req, res) => res.send("Hello World!"));

  app.get("/users", async (req, res) => {
    const users = await controller.getAllUsers(
      Boolean(req.query.include_deleted)
    );
    res.status(200).json(users);
  });

  app.get("/users/:name", async (req, res) => {
    const username = req.params.name;
    const user = await controller.getUserByName(
      username,
      Boolean(req.query.include_deleted)
    );
    if (user !== null) res.status(200).json(user);
    else res.status(404).send();
  });

  app.post("/users", async (req, res) => {
    const user = plainToClass(UserCreation, req.body);
    validate(user).then(async (errors) => {
      if (errors.length > 0) {
        let errorTexts = Array();
        for (const errorItem of errors) {
          errorTexts = errorTexts.concat(errorItem.constraints);
        }
        res.status(400).send(errorTexts.map(Object.values).flat());
        return;
      } else {
        res.status(201).json(await controller.createUser(user));
      }
    });
  });

  app.delete("/users/:name", async (req, res) => {
    const username = req.params.name;
    const user = await controller.deleteUserByName(username);
    if (user !== null) res.status(200).json(user);
    else res.status(404).send();
  });

  app.put("/users/:name", async (req, res) => {
    const username = req.params.name;
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
