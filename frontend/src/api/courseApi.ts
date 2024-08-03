import { Course } from '@root/dto';
import { api } from '.';

export const courseApi = api.injectEndpoints({
  endpoints: (build) => ({
    getCourses: build.query<Course[], void>({
      query: () => ({
        url: '/courses/',
      }),
    }),
    getCourseById: build.query<Course, number>({
      query: (id) => ({
        url: `/courses/${id}`,
      }),
    }),
  }),
  overrideExisting: false,
});

export const { useGetCoursesQuery, useGetCourseByIdQuery } = courseApi;
