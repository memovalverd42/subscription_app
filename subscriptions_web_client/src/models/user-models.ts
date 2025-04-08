export interface Token {
  access_token: string;
  token_type: string;
}

export interface UserBase {
  first_name: string | null;
  last_name: string | null;
  email: string;
}

export interface User extends UserBase {
  id: number;
}

export interface UserCreate extends UserBase {
  password: string;
}

export interface Session {
  user: User;
  token: Token;
}

export interface UserLogin {
  email: string;
  password: string;
}
