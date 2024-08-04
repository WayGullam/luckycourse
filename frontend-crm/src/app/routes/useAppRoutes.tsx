import { Navigate, RouteObject, useRoutes } from 'react-router-dom';
import { MainLayout } from '@/layouts/MainLayout/MainLayout';
import CoursesPage from '@/pages/Courses';
import LoginPage from '@/pages/Login';
import { useSelector } from 'react-redux';
import { selectIsAuthenticated } from '@/entities/session/sessionSlice';
import CourseConstructorPage from '@/pages/CourseConstructor';

const privateRoutes: RouteObject[] = [
  {
    path: '/',
    element: <MainLayout />,
    children: [
      {
        path: '/courses',
        element: <CoursesPage />,
      },
      {
        path: '/courses/create',
        element: <CourseConstructorPage />,
      },
      {
        path: '/courses/:courseId',
        element: <CourseConstructorPage />,
      },
    ],
  },
  {
    path: '*',
    element: <Navigate to='/' />,
  },
];

const publicRoutes: RouteObject[] = [
  {
    path: '/login',
    element: <LoginPage />,
  },
  {
    path: '*',
    element: <Navigate to='/login' />,
  },
];

export const useAppRoutes = () => {
  const isAuthenticated = useSelector(selectIsAuthenticated);
  const routes = useRoutes(isAuthenticated ? privateRoutes : publicRoutes);

  return routes;
};
