import fs from 'fs';
import path from 'path';
import { User } from '../interfaces/User';

export const usersDataFilePath = path.resolve(__dirname, '..', 'data', 'users.json');

export const createUsersDataFileIfNotExists = () => {
  if (!fs.existsSync(usersDataFilePath)) {
    fs.writeFileSync(usersDataFilePath, '[]');
  }
};

export const loadUsers = (): User[] => {
  const usersData = fs.readFileSync(usersDataFilePath).toString();
  const users = JSON.parse(usersData) as User[];
  return users;
};
