/* eslint-disable @typescript-eslint/no-explicit-any */
import { Course } from '@root/dto';
import { api } from '.';

export const courseApi = api.injectEndpoints({
  endpoints: (build) => ({
    getCourses: build.query<Course[], void>({
      query: () => ({
        url: '/courses/',
        method: 'GET',
      }),
      providesTags: ['Course'],
    }),
    deleteCourse: build.mutation<void, number>({
      query: (id) => ({
        url: `/courses/${id}/`,
        method: 'DELETE',
      }),
      invalidatesTags: ['Course'],
    }),
    createCourse: build.mutation<void, any>({
      query: (body) => ({
        url: '/courses/',
        method: 'POST',
        body,
      }),
      invalidatesTags: ['Course'],
    }),
  }),
});

export const { useGetCoursesQuery, useDeleteCourseMutation, useCreateCourseMutation } = courseApi;
