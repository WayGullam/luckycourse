import { PropsWithChildren } from 'react';
import { StoreProvider } from './StoreProvider';
import { BrowserRouter } from 'react-router-dom';
import { CssBaseline, CssVarsProvider } from '@mui/joy';

export const Providers = ({ children }: PropsWithChildren) => {
  return (
    <BrowserRouter>
      <CssVarsProvider>
        <CssBaseline />
        <StoreProvider>{children}</StoreProvider>
      </CssVarsProvider>
    </BrowserRouter>
  );
};
