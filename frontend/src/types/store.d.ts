import { type RootState as ReduxRootState } from '@/app/store';

declare global {
  interface RootState extends ReduxRootState {}
}
