/* eslint-disable @typescript-eslint/no-explicit-any */
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
    getUsers: build.query<any[], void>({
      query: () => ({
        url: '/profiles/',
      }),
      providesTags: ['User'],
    }),
    deleteUser: build.mutation<void, number>({
      query: (id) => ({
        url: `/profiles/${id}/`,
        method: 'DELETE',
      }),
      invalidatesTags: ['User'],
    }),
  }),
});

export const { useRegisterMutation, useLoginMutation, useGetUsersQuery, useDeleteUserMutation } =
  userApi;
