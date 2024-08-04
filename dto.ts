export type User = {
  id: number
  username: string
  first_name: string
  last_name: string
  role: Role
}

export enum Role {
  User = 1,
  Admin,
  Moderator
}

export type Progress = {
  id: number
  total: number
  completed: number
}

export type Course = {
  id: number
  title: string
  description: string
  imgPath: string
  modules: Module[]
  progress: Progress
  status: Status
}

export enum Status {
  NotStarted,
  InProgress,
  Completed
}

export enum QuestionType {
  Multiple = 1,
  Single,
  Input
}

export type Answer = {
  id: number
  question_id: number
  text: string
}

export type Question = {
  id: number
  title: string
  type: QuestionType
  answers?: Answer[]
}

export type QuestionWithAnswer = {
  question_id: number
  correct_answer: Answer
  user_answer: Answer
}

export type Test = {
  id: number
  title: string
  description: string
  questions: Question[]
  status: Status
}

export type Module = {
  id: number
  title: string
  description: string
  lessons: Lesson[]
  status: Status
}

export type Lesson = {
  id: number
  title: string
  description: string
  content: string
  status: Status
}
