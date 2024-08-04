import { UsersTable } from '@/entities/user/ui/UsersTable/UsersTable';
import { PageTitle } from '@/shared/ui/PageTitle';
import { Box } from '@mui/joy';

const UsersPage = () => {
  return (
    <Box width='100%'>
      <PageTitle hideBtn title='Пользователи' />
      <Box mt={2}>
        <UsersTable />
      </Box>
    </Box>
  );
};

export default UsersPage;
