import * as express from "express";
import * as UserController from "./userController";
import { UserPost } from "./payloads";
import { validate } from "class-validator";
import { plainToClass } from "class-transformer";

export const register = (app: express.Application) => {
  app.get("/", (req, res) => res.send("Hello World!"));

  app.get("/users", (req, res) => {
    let users = UserController.listUsers();
    if (req.query.name !== undefined)
      users = users.filter((user) => user.name == req.query.name);
    // if (req.query.include_deleted === "true" || )
    //   users = users.filter((user) => user.name == req.query.name);
    res.status(200).json(users);
  });

  app.get("/users/:id", (req, res) => {
    const userId = Number(req.params.id);
    res.status(200).json(UserController.findUser(userId));
  });

  app.post("/users", (req, res) => {
    const user = plainToClass(UserPost, req.body);
    validate(user).then((errors) => {
      // errors is an array of validation errors
      if (errors.length > 0) {
        let errorTexts = Array();
        for (const errorItem of errors) {
          errorTexts = errorTexts.concat(errorItem.constraints);
        }
        res.status(400).send(errorTexts);
        return;
      } else {
        // pass 'user' object to repository/service
        res.status(200).json(UserController.addUser(user));
      }
    });
  });

  app.delete("/users/:id", (req, res) => {
    const userId = Number(req.params.id);
    res.status(200).json(UserController.deleteUser(userId));
  });

  app.put("/users/:id", (req, res) => {
    const userId = Number(req.params.id);
    const toUpdate = req.body;
    res.status(200).json(UserController.updateUser(userId, toUpdate));
  });
};
