import { Course } from '@root/dto';
import { api } from '.';

export const courseApi = api.injectEndpoints({
  endpoints: (build) => ({
    getCourses: build.query<Course[], void>({
      query: () => ({
        url: '/courses/',
      }),
    }),
  }),
});

export const { useGetCoursesQuery } = courseApi;
