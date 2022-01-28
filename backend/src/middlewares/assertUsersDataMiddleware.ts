import { NextFunction, Request, Response } from 'express';
import { createUsersDataFileIfNotExists } from '../utils/users';

export const assertUsersDataMiddleware = (_: Request, __: Response, next: NextFunction) => {
  createUsersDataFileIfNotExists();
  return next();
};
