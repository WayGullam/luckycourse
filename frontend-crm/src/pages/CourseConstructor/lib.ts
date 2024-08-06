/* eslint-disable @typescript-eslint/no-unused-vars */
import { CourseConstructorFormState } from './types';

export const serizalizeCourseConstructorFormState = ({
  img,
  ...values
}: CourseConstructorFormState) => {
  return {
    ...values,
    img_url: img,
    modules: values.modules.map(({ id, ...module }) => ({
      ...module,
      lessons: module.lessons?.map(({ id, ...lesson }) => ({
        ...lesson,
      })),
      test: {
        ...module.test,
        questions: module.test.questions?.map(({ id, ...question }) => ({
          ...question,
          answers: question.answers?.map(({ id, ...answer }) => ({
            ...answer,
          })),
        })),
      },
    })),
  };
};
