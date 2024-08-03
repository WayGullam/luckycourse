import { AppDispatch, type RootState as ReduxRootState } from '@/app/store';
import { type UseDispatch, type UseSelector } from 'react-redux';

declare global {
  export interface RootState extends ReduxRootState {}
}

declare module 'react-redux' {
  declare const useSelector: UseSelector<ReduxRootState>;
  declare const useDispatch: UseDispatch<AppDispatch>;
}
