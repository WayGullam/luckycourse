import { Auth } from '@/pages/Auth/Auth';
import { Registration } from '@/pages/Auth/Registration';
import { CoursePage } from '@/pages/CoursePage';
import { MainPage } from 'pages/MainPage';
import { RouteProps } from 'react-router-dom';

export enum AppRoutes {
  MAIN = 'main',
  COURSE = 'courses',
  AUTH = 'auth',
  REGISTRATION = 'registration',
}

export const RouterPath: Record<AppRoutes, string> = {
  [AppRoutes.MAIN]: '/',
  [AppRoutes.COURSE]: '/courses/:courseId',
  [AppRoutes.AUTH]: '/auth',
  [AppRoutes.REGISTRATION]: '/registration',
};

export const routerConfig: Record<AppRoutes, RouteProps> = {
  [AppRoutes.MAIN]: {
    path: RouterPath.main,
    element: <MainPage />,
  },
  [AppRoutes.COURSE]: {
    path: RouterPath.courses,
    element: <CoursePage />,
  },

  [AppRoutes.AUTH]: {
    path: RouterPath.auth,
    element: <Auth />,
  },
  [AppRoutes.REGISTRATION]: {
    path: RouterPath.registration,
    element: <Registration />,
  },
};
