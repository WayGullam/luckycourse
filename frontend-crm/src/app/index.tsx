import { GlobalStyles } from '@mui/joy';
import { Providers } from './providers';
import { Routes } from './routes';

export const App = () => {
  return (
    <Providers>
      <GlobalStyles
        styles={(theme) => ({
          '.ck-editor__editable_inline': {
            minHeight: 200,
          },
          '.ck-powered-by': {
            display: 'none',
          },
          '.MuiModal-root': {
            [theme.breakpoints.up('md')]: {
              width: 'calc(100dvw - var(--Sidebar-width))',
              marginLeft: 'var(--Sidebar-width)',
            },
          },
        })}
      />
      <Routes />
    </Providers>
  );
};

export default App;
