import { User } from "./user";

export interface ReqBodyUser extends User {
  confirm_password: string;
}
