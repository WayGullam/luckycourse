import { Test as TTest } from '@root/dto';
import { useLocation } from 'react-router-dom';
import { Test } from './components/Test';

const ModuleTestPage = () => {
  const location = useLocation();
  const test = location.state as TTest;

  return <Test test={test} />;
};

export default ModuleTestPage;
