import { ToastContainer } from 'react-toastify';
import { Providers } from './providers';
import 'react-toastify/dist/ReactToastify.css';

export const App = () => {
  return (
    <Providers>
      <ToastContainer />
      App
    </Providers>
  );
};
