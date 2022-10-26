import Database from "better-sqlite3";
import fs from "fs";
import { User } from "./model";

export default class UserRepository {
  db: Database.Database;

  constructor() {
    this.db = new Database("db/users.db", { verbose: console.log });
    this.applyMigrations();
  }

  //Table creation
  applyMigrations(): void {
    const applyMigration = (path: string) => {
      const migration = fs.readFileSync(path, "utf8");
      this.db.exec(migration);
    };

    const testRow = this.db
      .prepare(
        "SELECT name FROM sqlite_schema WHERE type = 'table' AND name = 'users'"
      )
      .get();

    if (!testRow) {
      console.log("Applying migrations on DB users...");
      const migrations = ["db/migrations/init.sql"];
      migrations.forEach(applyMigration);
    }
  }

  getAllUsers(include_deleted: boolean = false): User[] {
    const statement = this.db.prepare(
      "SELECT * FROM users" + (!include_deleted ? " WHERE NOT is_deleted" : "")
    );
    return statement.all() as User[];
  }

  getUserById(userId: number, include_deleted: boolean = false): User {
    const statement = this.db.prepare(
      "SELECT * FROM users WHERE user_id = ?" +
        (!include_deleted ? " AND NOT is_deleted" : "")
    );
    return statement.get(userId) as User;
  }

  createUser(name: string): number {
    const statement = this.db.prepare("INSERT INTO users (name) VALUES (?)");
    return Number(statement.run(name).lastInsertRowid);
  }

  deleteUserById(userId: number): void {
    this.db
      .prepare("UPDATE users SET is_deleted = TRUE WHERE user_id = ?")
      .run(userId);
  }

  updateUser(user: User): void {
    console.log(user);
    this.db
      .prepare("UPDATE users SET name = ? WHERE user_id = ?")
      .run(user.name, user.user_id);
  }
}
