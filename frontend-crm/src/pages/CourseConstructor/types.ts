import { QuestionType } from '@root/dto';

export type CourseConstructorFormState = {
  title: string;
  description: string;
  img: string;
  modules: {
    id: number;
    title: string;
    description: string;
    lessons?: { id: number; title: string; description: string; content: string }[];
    test: {
      title: string;
      description: string;
      questions: {
        id: number;
        text: string;
        type: QuestionType;
        answers: { id: number; text?: string; is_correct: boolean }[];
      }[];
    };
  }[];
};
