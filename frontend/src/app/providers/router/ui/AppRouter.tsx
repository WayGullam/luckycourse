import { selectIsAuthenticated } from '@/entities/session/sessionSlice';
import { Suspense } from 'react';
import { useSelector } from 'react-redux';
import { Route, Routes } from 'react-router-dom';
import { priviteRouterConfig } from 'shared/config/routerConfig/priviteRouterConfig';
import { publicRouterConfig } from 'shared/config/routerConfig/publicRouterConfig';

const AppRouter = () => {
  const isAuthenticated = useSelector(selectIsAuthenticated);

  return (
    <Suspense fallback={<div>Loading...</div>}>
      <Routes>
        {Object.values(isAuthenticated ? priviteRouterConfig : publicRouterConfig).map(
          ({ element, path }) => (
            <Route
              key={path}
              path={path}
              element={
                <Suspense fallback={<div>Loading...</div>}>
                  <div className='page-wrapper'>{element}</div>
                </Suspense>
              }
            />
          ),
        )}
      </Routes>
    </Suspense>
  );
};

export default AppRouter;
