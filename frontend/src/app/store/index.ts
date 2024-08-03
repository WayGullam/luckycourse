import { configureStore } from '@reduxjs/toolkit';
import { api } from '@/api';
import { sessionSlice } from '@/entities/session/sessionSlice';

const store = configureStore({
  reducer: { [api.reducerPath]: api.reducer, [sessionSlice.reducerPath]: sessionSlice.reducer },
});

export type RootState = ReturnType<typeof store.getState>;

export default store;
