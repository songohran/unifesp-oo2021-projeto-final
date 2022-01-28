import express from 'express';

import { authRouter } from './routes/auth';
import { usersRouter } from './routes/users';
import { assertUsersDataMiddleware } from './middlewares/assertUsersDataMiddleware';

const app = express();

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.use('/users', assertUsersDataMiddleware, usersRouter);
app.use('/auth', assertUsersDataMiddleware, authRouter);

app.use('/', (_, res) => {
  res.redirect('/frontend/public');
});

export { app };
