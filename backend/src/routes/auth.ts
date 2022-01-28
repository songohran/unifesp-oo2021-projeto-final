import { Router } from 'express';
import { compare } from 'bcrypt';

import { loadUsers } from '../utils/users';
import { ReqBodyUser } from '../interfaces/ReqBodyUser';

const authRouter = Router();

authRouter.post('/login', async (req, res) => {
  const users = loadUsers();
  const reqBody = req.body as ReqBodyUser;
  const findedUser = users.find((u) => u.cpf === reqBody.cpf);

  if (findedUser) {
    const matchPassword = await compare(reqBody.password, findedUser.password);

    if (matchPassword) {
      return res.status(200).send('Usuário OK');
    }

    return res.status(401).send('Senha incorreta');
  }

  return res.status(404).send('Usuário não encontrado');
});

export { authRouter };
