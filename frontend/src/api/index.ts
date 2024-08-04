import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';

const API_URL = 'http://192.168.17.16:8000';

// Create our baseQuery instance
const baseQuery = fetchBaseQuery({
  baseUrl: API_URL,
  prepareHeaders: (headers, { getState }) => {
    const token = (getState() as RootState).session.token;
    if (token) {
      headers.set('authorization', `Token ${token}`);
    }
    return headers;
  },
});

const baseQueryWithRetry = baseQuery;

export const api = createApi({
  reducerPath: 'api',
  baseQuery: baseQueryWithRetry,
  tagTypes: ['User'],
  endpoints: () => ({}),
});
