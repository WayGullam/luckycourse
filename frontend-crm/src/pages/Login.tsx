import { Box, Button, FormControl, Grid, Input, Sheet } from '@mui/joy';

const LoginPage = () => {
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
          borderRadius: theme.radius.md,
        })}
      >
        <Grid component='form' container spacing={1.5}>
          <Grid component='div' xs={12}>
            <FormControl size='sm'>
              <Input
                fullWidth
                autoFocus
                name='login'
                placeholder='Логин'
                autoComplete='on'
                variant='outlined'
              />
            </FormControl>
          </Grid>
          <Grid component='div' xs={12}>
            <FormControl size='sm'>
              <Input fullWidth name='password' placeholder='Пароль' variant='outlined' />
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
