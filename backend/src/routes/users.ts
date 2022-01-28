import fs from "fs/promises";
import { Router } from "express";
import { hash } from "bcrypt";

import { loadUsers, usersDataFilePath } from "../utils/users";
import { ReqBodyUser } from "../interfaces/req-body-user";

const usersRouter = Router();

usersRouter.get("/", (_, res) => {
  const users = loadUsers();
  return res.status(200).json(users);
});

usersRouter.get("/:cpf", (req, res) => {
  const { cpf } = req.params;
  const users = loadUsers();
  const findedUser = users.find((u) => u.cpf === cpf);

  if (findedUser) {
    return res.status(200).json(findedUser);
  }

  return res.status(404).send("Usuário não encontrado");
});

usersRouter.post("/", async (req, res) => {
  const users = loadUsers();
  const reqBody = req.body as ReqBodyUser;

  if (users.some((user) => user.cpf === reqBody.cpf)) {
    return res.status(400).send("CPF já cadastrado");
  }

  const hashedPassword = await hash(reqBody.password, 8);
  reqBody.password = hashedPassword;

  const { confirm_password: _, ...user } = reqBody;
  users.push(user);

  await fs.writeFile(usersDataFilePath, JSON.stringify(users));

  return res.status(201).send("Cadastro realizado com sucesso!");
});

export { usersRouter };
