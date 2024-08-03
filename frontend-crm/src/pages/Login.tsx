import { RequestAuthBody } from '@/api/types';
import { useLoginMutation } from '@/api/userApi';
import { Box, Button, FormControl, Grid, Input, Sheet } from '@mui/joy';
import { useForm } from 'react-hook-form';

const LoginPage = () => {
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
    <Box
      sx={{
        width: '100dvw',
        height: '100dvh',
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
      }}
    >
      <Sheet
        sx={(theme) => ({
          margin: '0 auto',
          width: '100%',
          maxWidth: '400px',
          padding: 2,
          borderRadius: theme.radius.sm,
        })}
      >
        <Grid component='form' container spacing={1.5} onSubmit={form.handleSubmit(authHandler)}>
          <Grid component='div' xs={12}>
            <FormControl size='sm'>
              <Input
                fullWidth
                autoFocus
                placeholder='Логин'
                autoComplete='on'
                variant='outlined'
                {...form.register('username')}
              />
            </FormControl>
          </Grid>
          <Grid component='div' xs={12}>
            <FormControl size='sm'>
              <Input
                fullWidth
                placeholder='Пароль'
                variant='outlined'
                {...form.register('password')}
              />
            </FormControl>
          </Grid>
          <Grid component='div' xs={12}>
            <Button fullWidth type='submit' color='primary'>
              Войти
            </Button>
          </Grid>
        </Grid>
      </Sheet>
    </Box>
  );
};

export default LoginPage;
