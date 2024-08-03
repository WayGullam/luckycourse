import { RouteObject, useRoutes } from 'react-router-dom';
import { MainLayout } from '@/layouts/MainLayout/MainLayout';
import CoursesPage from '@/pages/Courses';
import LoginPage from '@/pages/Login';
import { useSelector } from 'react-redux';
import { selectIsAuthenticated } from '@/entities/session/sessionSlice';

const privateRoutes: RouteObject[] = [
  {
    path: '/',
    element: <MainLayout />,
    children: [
      {
        path: '/courses',
        element: <CoursesPage />,
      },
    ],
  },
];

const publicRoutes: RouteObject[] = [
  {
    path: '/login',
    element: <LoginPage />,
  },
];

export const useAppRoutes = () => {
  const isAuthenticated = useSelector(selectIsAuthenticated);
  const routes = useRoutes(isAuthenticated ? privateRoutes : publicRoutes);

  return routes;
};
