import * as mongoDB from "mongodb";
import got from "got";
import { Static } from "runtypes";
import { User } from "./model.js";
import { UserCreation, UserLogin } from "./payloads.js";

const DB_CONN_STRING = "mongodb://mongo:27017";
const DB_NAME = "users";
const AUTH_URL = "http://auth";

export default class UserController {
  client: mongoDB.MongoClient;

  constructor() {
    this.client = new mongoDB.MongoClient(DB_CONN_STRING);
  }

  async getCollection(collection_name: string): Promise<mongoDB.Collection> {
    await this.client.connect();
    const db = this.client.db(DB_NAME);
    const collection = db.collection(collection_name);
    return collection;
  }

  async getAllUsers(include_deleted: boolean = false): Promise<User[]> {
    const collection = await this.getCollection("users");
    const filter = include_deleted ? {} : { is_deleted: false };
    return (await collection
      .find<User>(filter, { projection: { _id: false, token: false } })
      .toArray()) as User[];
  }

  async getUserByName(
    name: string,
    include_deleted: boolean = false
  ): Promise<User> {
    const collection = await this.getCollection("users");
    const filter = include_deleted ? { name } : { name, is_deleted: false };
    return (await collection.findOne<User>(filter, {
      projection: { _id: false, token: false },
    })) as User;
  }

  async getUserToken(login: Static<typeof UserLogin>) {
    const collection = await this.getCollection("users");
    try {
      const { token: token_auth } = (await got
        .post(`${AUTH_URL}/authenticate`, {
          json: {
            username: login.name,
            password: login.password,
          },
        })
        .json()) as {
        token: string;
      };
      const { token: token_db } = await collection.findOne<{ token: string }>(
        { name: login.name },
        {
          projection: { token: true },
        }
      );
      if (token_auth !== token_db) return "";
      return token_auth;
    } catch (err) {
      console.error(err);
    }
    return "";
  }

  async createUser(user: Static<typeof UserCreation>): Promise<string> {
    const collection = await this.getCollection("users");
    try {
      const { token } = (await got
        .post(`${AUTH_URL}/authenticate`, {
          json: {
            username: user.name,
            password: user.password,
          },
        })
        .json()) as {
        token: string;
      };
      await collection.insertOne({
        name: user.name,
        email: user.email,
        role: user.role,
        badges: [],
        is_deleted: false,
        token,
      });
      return token;
    } catch (err) {
      console.error(err);
    }
    return "";
  }

  async deleteUserByName(name: string): Promise<void> {
    const collection = await this.getCollection("users");
    await collection.updateOne({ name }, { $set: { is_deleted: true } });
  }

  async updateUser(
    name: string,
    to_update: Partial<Omit<User, "name">>
  ): Promise<void> {
    const collection = await this.getCollection("users");
    await collection.updateOne({ name }, { $set: to_update });
  }

  async getUsernameFromToken(token: string) {
    try {
      const { username } = (await got
        .get(`${AUTH_URL}/user-context/${token}`)
        .json()) as {
        username: string;
      };
      const user = await this.getUserByName(username);
      if (user !== null) return username;
    } catch (err) {
      console.error(err);
    }
    return "";
  }

  async getRoleFromToken(token: string) {
    try {
      const { username } = (await got
        .get(`${AUTH_URL}/user-context/${token}`)
        .json()) as {
        username: string;
      };
      const user = await this.getUserByName(username);
      if (user !== null) return user.role;
    } catch (err) {
      console.error(err);
    }
    return "";
  }
}
