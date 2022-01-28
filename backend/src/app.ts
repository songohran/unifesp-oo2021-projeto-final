import express, { NextFunction, Request, Response } from "express";
import path from "path";
import { createUsersDataFileIfNotExists } from "./utils/users";

import { authRouter } from "./routes/auth";
import { usersRouter } from "./routes/users";

const app = express();
const frontendPublic = path.resolve(__dirname, "..", "..", "frontend", "public");

const assertUsersDataMiddleware = (_: Request, __: Response, next: NextFunction) => {
  createUsersDataFileIfNotExists();
  return next();
};

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.use("/frontend/public", express.static(frontendPublic));

app.use("/users", assertUsersDataMiddleware, usersRouter);
app.use("/auth", assertUsersDataMiddleware, authRouter);

app.use("/", (_, res) => {
  res.redirect("/frontend/public");
});

export { app };
