import express from 'express';
import path from 'path';

import { authRouter } from './routes/auth';
import { usersRouter } from './routes/users';
import { assertUsersDataMiddleware } from './middlewares/assertUsersDataMiddleware';

const app = express();

const pagesPath = path.resolve(__dirname, '..', '..', 'frontend', 'pages');
const assetsPath = path.resolve(pagesPath, '..', 'assets');

app.use('/pages', express.static(pagesPath));
app.use('/assets', express.static(assetsPath));

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.use('/users', assertUsersDataMiddleware, usersRouter);
app.use('/auth', assertUsersDataMiddleware, authRouter);

app.use('/', (_, res) => {
  res.redirect('/pages');
});

export { app };
