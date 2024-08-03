import React from 'react';
import styled from 'styled-components';
import { Container, TextField, Button, Typography, Box, Avatar, CssBaseline } from '@mui/material';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';

const StyledContainer = styled(Container)`
  margin-top: 8px;
  display: flex;
  flex-direction: column;
  align-items: center;
`;

const StyledAvatar = styled(Avatar)`
  margin: 8px;
  background-color: #3f51b5; /* Синий цвет */
`;

const StyledButton = styled(Button)`
  margin-top: 24px;
  margin-bottom: 16px;
  background-color: #3f51b5; /* Синий цвет */
  &:hover {
    background-color: #303f9f; /* Темно-синий цвет */
  }
`;

export const Auth = () => {
  return (
    <Container component='main' maxWidth='xs'>
      <CssBaseline />
      <StyledContainer>
        <Typography component='h1' variant='h5'>
          Авторизация
        </Typography>
        <Box component='form' noValidate sx={{ mt: 1 }}>
          <TextField
            margin='normal'
            required
            fullWidth
            id='email'
            label='Email адрес'
            name='email'
            autoComplete='email'
            autoFocus
          />
          <TextField
            margin='normal'
            required
            fullWidth
            name='password'
            label='Пароль'
            type='password'
            id='password'
            autoComplete='current-password'
          />
          <StyledButton type='submit' fullWidth variant='contained'>
            Войти
          </StyledButton>
        </Box>
      </StyledContainer>
    </Container>
  );
};
