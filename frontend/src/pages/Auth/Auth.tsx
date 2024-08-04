import { Typography, Box } from '@mui/material';
import * as Styled from './Auth.styled';
import { useLoginMutation } from '@/api/userApi';
import { useForm } from 'react-hook-form';
import { RequestAuthBody } from '@/api/types';

export const Auth = () => {
  const [login] = useLoginMutation();

  const form = useForm<RequestAuthBody>({
    defaultValues: {
      username: '',
      password: '',
    },
  });

  const authHandler = async (values: RequestAuthBody) => {
    login(values);
  };

  return (
    <Styled.FullHeightBox>
      <Styled.StyledFormContainer>
        <Typography component='h1' variant='h5'>
          Вход
        </Typography>
        <Box component='form' noValidate sx={{ mt: 1 }} onSubmit={form.handleSubmit(authHandler)}>
          <Styled.StyledTextField
            margin='normal'
            required
            fullWidth
            id='login'
            label='Логин'
            autoComplete='login'
            sx={{ mb: 2 }}
            {...form.register('username')}
          />
          <Styled.StyledTextField
            margin='normal'
            required
            fullWidth
            label='Пароль'
            type='password'
            id='password'
            autoComplete='current-password'
            sx={{ mb: 2 }}
            {...form.register('password')}
          />
          <Styled.StyledButton type='submit' fullWidth variant='contained'>
            Войти
          </Styled.StyledButton>
        </Box>
      </Styled.StyledFormContainer>
    </Styled.FullHeightBox>
  );
};
