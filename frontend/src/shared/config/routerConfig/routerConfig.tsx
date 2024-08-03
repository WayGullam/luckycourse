import { Auth } from '@/pages/Auth/Auth';
import { Log } from '@/pages/Auth/Log';
import { CoursePage } from '@/pages/CoursePage';
import { MainPage } from 'pages/MainPage';
import { RouteProps } from 'react-router-dom';

export enum AppRoutes {
  MAIN = 'main',
  COURSE = 'course',
  AUTH = 'auth',
  LOGIN = 'login',
}

export const RouterPath: Record<AppRoutes, string> = {
  [AppRoutes.MAIN]: '/',
  [AppRoutes.COURSE]: '/course',
  [AppRoutes.AUTH]: '/auth',
  [AppRoutes.LOGIN]: '/login',
};

export const routerConfig: Record<AppRoutes, RouteProps> = {
  [AppRoutes.MAIN]: {
    path: RouterPath.main,
    element: <MainPage />,
  },
  [AppRoutes.COURSE]: {
    path: RouterPath.course,
    element: <CoursePage />,
  },
  [AppRoutes.AUTH]: {
    path: RouterPath.auth,
    element: <Auth />,
  },
  [AppRoutes.LOGIN]: {
    path: RouterPath.login,
    element: <Log />,
  },
};
