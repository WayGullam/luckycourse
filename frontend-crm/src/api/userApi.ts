import { User } from '@root/dto';
import { api } from '.';
import { RequestAuthBody } from './types';

export const userApi = api.injectEndpoints({
  endpoints: (build) => ({
    login: build.mutation<{ token: string }, RequestAuthBody>({
      query: (body) => ({
        body,
        url: '/auth/',
        method: 'POST',
      }),
    }),
    register: build.mutation<{ token: string }, Omit<User, 'user'>>({
      query: (body) => ({
        body,
        url: '/register/',
        method: 'POST',
      }),
    }),
  }),
});

export const { useRegisterMutation, useLoginMutation } = userApi;
