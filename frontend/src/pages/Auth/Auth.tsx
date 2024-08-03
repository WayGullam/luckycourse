import { Typography, Box } from '@mui/material';
import * as Styled from './Auth.styled';

export const Auth = () => {
  return (
    <Styled.FullHeightBox>
      <Styled.StyledFormContainer>
        <Typography component='h1' variant='h5'>
          Вход
        </Typography>
        <Box component='form' noValidate sx={{ mt: 1 }}>
          <Styled.StyledTextField
            margin='normal'
            required
            fullWidth
            id='login'
            label='Логин'
            name='логин'
            autoComplete='логин'
            sx={{ mb: 2 }}
          />
          <Styled.StyledTextField
            margin='normal'
            required
            fullWidth
            name='password'
            label='Пароль'
            type='password'
            id='password'
            autoComplete='current-password'
            sx={{ mb: 2 }}
          />
          <Styled.StyledButton type='submit' fullWidth variant='contained'>
            Войти
          </Styled.StyledButton>
        </Box>
      </Styled.StyledFormContainer>
    </Styled.FullHeightBox>
  );
};
