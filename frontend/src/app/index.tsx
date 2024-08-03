import { ToastContainer } from 'react-toastify';
import { Providers } from './providers';
import 'react-toastify/dist/ReactToastify.css';
import { Suspense } from 'react';
import { AppRouter } from './providers/router';
import { Navbar } from '@/widgets/Navbar';

import './styles/index.scss';
import { MainLayout } from '@/Layouts/MainLayout/ui/MainLayout';
import { CssBaseline } from '@mui/material';

export const App = () => {
  return (
    <Providers>
      <CssBaseline />
      <ToastContainer />
      <Suspense fallback=''>
        <Navbar />
        <MainLayout>
          <div className='content-page'>
            <AppRouter />
          </div>
        </MainLayout>
      </Suspense>
    </Providers>
  );
};
