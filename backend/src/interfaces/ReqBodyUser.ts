import { User } from './User';

export interface ReqBodyUser extends User {
  // eslint-disable-next-line
  confirm_password: string;
}
