import styled from 'styled-components';
import { TextField, Button, Typography, Box, Paper } from '@mui/material';

const FullHeightBox = styled(Box)`
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
`;

const StyledFormContainer = styled(Paper)`
  padding: 24px;
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  max-width: 400px;
  box-shadow: 0px 3px 6px rgba(0, 0, 0, 0.16);
  border-radius: 12px;
`;

const StyledTextField = styled(TextField)`
  & .MuiOutlinedInput-root {
    border-radius: 12px;
  }
`;

const StyledButton = styled(Button)`
  margin-top: 24px;
  margin-bottom: 16px;
  background-color: #3f51b5;
  border-radius: 12px;
  &:hover {
    background-color: #303f9f;
  }
`;

export const Log = () => {
  return (
    <FullHeightBox>
      <StyledFormContainer>
        <Typography component='h1' variant='h5'>
          Вход
        </Typography>
        <Box component='form' noValidate sx={{ mt: 1 }}>
          <StyledTextField
            margin='normal'
            required
            fullWidth
            id='login'
            label='Логин'
            name='логин'
            autoComplete='логин'
            sx={{ mb: 2 }}
          />
          <StyledTextField
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
          <StyledButton type='submit' fullWidth variant='contained'>
            Войти
          </StyledButton>
        </Box>
      </StyledFormContainer>
    </FullHeightBox>
  );
};
