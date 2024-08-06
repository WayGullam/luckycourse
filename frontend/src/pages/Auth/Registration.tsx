import { Typography, Box } from '@mui/material';
import * as Styled from './Auth.styled';
import { useRegisterMutation } from '@/api/userApi';
import { RequestRegistBody } from '@/api/types';
import { useForm } from 'react-hook-form';
import { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

export const Registration = () => {
  const [register, status] = useRegisterMutation();
  const navigate = useNavigate();

  const form = useForm<RequestRegistBody>({
    defaultValues: {
      first_name: '',
      last_name: '',
      username: '',
      password: '',
    },
  });

  const authHandler = async (values: RequestRegistBody) => {
    register(values);
  };

  useEffect(() => {
    if (status.isUninitialized) {
      navigate('/');
    }
  }, [status.isUninitialized]);

  return (
    <Styled.FullHeightBox>
      <Styled.StyledFormContainer sx={{ borderRadius: 4, boxShadow: '0 0 30px 10px #00000020' }}>
        <Typography component='h1' variant='h5'>
          Регистрация
        </Typography>
        <Box component='form' noValidate sx={{ mt: 1 }} onSubmit={form.handleSubmit(authHandler)}>
          <Styled.StyledTextField
            margin='normal'
            required
            fullWidth
            id='last_name'
            label='Фамилия'
            autoComplete='last_name'
            autoFocus
            sx={{ mb: 2 }}
            {...form.register('last_name')}
          />
          <Styled.StyledTextField
            margin='normal'
            required
            fullWidth
            id='first_name'
            label='Имя'
            autoComplete='first_name'
            sx={{ mb: 2 }}
            {...form.register('first_name')}
          />
          <Styled.StyledTextField
            margin='normal'
            required
            fullWidth
            id='username'
            label='Логин'
            autoComplete='username'
            {...form.register('username')}
            sx={{ mb: 2 }}
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
          <Styled.StyledButton type='submit' fullWidth variant='contained' sx={{ borderRadius: 2 }}>
            ЗАРЕГИСТРИРОВАТЬСЯ
          </Styled.StyledButton>
        </Box>
      </Styled.StyledFormContainer>
    </Styled.FullHeightBox>
  );
};
