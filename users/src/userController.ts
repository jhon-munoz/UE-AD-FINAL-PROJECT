import * as mongoDB from "mongodb";
import { User } from "./model";

const DB_CONN_STRING = "mongodb://mongo:27017";
const DB_NAME = "users";

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
      .find<User>(filter, { projection: { _id: false } })
      .toArray()) as User[];
  }

  async getUserByName(
    name: string,
    include_deleted: boolean = false
  ): Promise<User> {
    const collection = await this.getCollection("users");
    const filter = include_deleted ? { name } : { name, is_deleted: false };
    return (await collection.findOne<User>(filter, {
      projection: { _id: false },
    })) as User;
  }

  async createUser(user: Omit<User, "badges">): Promise<User> {
    const collection = await this.getCollection("users");
    await collection.insertOne({ ...user, badges: [], is_deleted: false });
    return { ...user, badges: [] };
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
}
