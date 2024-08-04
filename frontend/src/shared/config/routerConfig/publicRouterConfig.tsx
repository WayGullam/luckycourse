import { Auth } from '@/pages/Auth/Auth';
import { Registration } from '@/pages/Auth/Registration';
import { Navigate, RouteProps } from 'react-router-dom';

export enum AppRoutes {
  AUTH = 'auth',
  ALL = 'all',
}

export const RouterPath: Record<AppRoutes, string> = {
  [AppRoutes.AUTH]: '/auth',
  [AppRoutes.ALL]: '*',
};

export const publicRouterConfig: Record<AppRoutes, RouteProps> = {
  [AppRoutes.AUTH]: {
    path: RouterPath.auth,
    element: <Auth />,
  },
  [AppRoutes.ALL]: {
    path: RouterPath.all,
    element: (
      <>
        <Navigate to='/registration' /> <Registration />
      </>
    ),
  },
};
