import { ToastContainer } from 'react-toastify';
import { Providers } from './providers';
import 'react-toastify/dist/ReactToastify.css';
import { Suspense } from 'react';
import { AppRouter } from './providers/router';

export const App = () => {
  return (
    <Providers>
      <ToastContainer />
      <Suspense fallback=''>
        <div className='content-page'>
          <AppRouter />
        </div>
      </Suspense>
    </Providers>
  );
};
