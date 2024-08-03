import { createSlice } from '@reduxjs/toolkit';
import { userApi } from '@/api/userApi';

export const SESSION_KEY = 'session';

export type SessionState = {
  token: string | null;
  isAuthenticated: boolean;
};

const state = localStorage.getItem(SESSION_KEY);

const getInitialState = (): SessionState =>
  state
    ? JSON.parse(state)
    : {
        isAuthenticated: false,
        token: null,
      };

export const sessionSlice = createSlice({
  name: 'session',
  initialState: getInitialState(),
  reducers: {
    logout: () => {
      localStorage.removeItem(SESSION_KEY);
      return {
        client: null,
        isAuthenticated: false,
        token: null,
      };
    },
  },
  extraReducers: (builder) => {
    builder.addMatcher(userApi.endpoints.login.matchFulfilled, (state, action) => {
      state.token = action.payload.token;
      state.isAuthenticated = !!action.payload.token;
      localStorage.setItem(SESSION_KEY, JSON.stringify(state));
    });
    builder.addMatcher(userApi.endpoints.register.matchFulfilled, (state, action) => {
      state.token = action.payload.token;
      state.isAuthenticated = true;
      localStorage.setItem(SESSION_KEY, JSON.stringify(state));
    });
  },
});

export const { logout } = sessionSlice.actions;

export const selectIsAuthenticated = (state: RootState) => state.session.isAuthenticated;
