import { PropsWithChildren } from 'react';
import { StoreProvider } from './StoreProvider';
import { BrowserRouter } from 'react-router-dom';
import { CssBaseline, CssVarsProvider } from '@mui/joy';
import { ToastContainer } from 'react-toastify';

export const Providers = ({ children }: PropsWithChildren) => {
  return (
    <BrowserRouter>
      <ToastContainer limit={2} autoClose={2000} />
      <CssVarsProvider>
        <CssBaseline />
        <StoreProvider>{children}</StoreProvider>
      </CssVarsProvider>
    </BrowserRouter>
  );
};
