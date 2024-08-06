import { Typography, Box } from '@mui/material';
import * as Styled from './Auth.styled';
import { useLoginMutation } from '@/api/userApi';
import { useForm } from 'react-hook-form';
import { RequestAuthBody } from '@/api/types';
import { useNavigate } from 'react-router-dom';
import { useEffect } from 'react';

export const Auth = () => {
  const [login, status] = useLoginMutation();
  const navigate = useNavigate();

  const form = useForm<RequestAuthBody>({
    defaultValues: {
      username: '',
      password: '',
    },
  });

  const authHandler = async (values: RequestAuthBody) => {
    login(values);
  };

  useEffect(() => {
    if (status.isSuccess) {
      navigate('/');
    }
  }, [status.isSuccess]);

  return (
    <Styled.FullHeightBox>
      <Styled.StyledFormContainer sx={{borderRadius: 4, boxShadow: '0 0 30px 10px #00000020'}}>
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
          <Styled.StyledButton type='submit' fullWidth variant='contained' sx={{borderRadius: 2}}>
            ВОЙТИ
          </Styled.StyledButton>
        </Box>
      </Styled.StyledFormContainer>
    </Styled.FullHeightBox>
  );
};
