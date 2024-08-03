import { CoursesTable } from '@/entities/course/ui/CoursesTable';
import { PageTitle } from '@/shared/ui/PageTitle';
import { Box, Button, Grid, Input, Sheet } from '@mui/joy';
import { IconSearch } from '@tabler/icons-react';

function CoursesPage() {
  return (
    <Box width='100%'>
      <PageTitle title='Курсы' />
      <Box mt={4} width={200}>
        <Button fullWidth variant='outlined' color='warning'>
          Фильтры
        </Button>
      </Box>
      <Sheet
        sx={(theme) => ({
          width: '100%',
          padding: 2,
          mt: 2,
          borderRadius: theme.radius.sm,
          bgcolor: theme.palette.warning.softBg,
        })}
      >
        <Grid container>
          <Grid xs={4}>
            <Input placeholder='Поиск' sx={{ bgcolor: 'white' }} startDecorator={<IconSearch />} />
          </Grid>
        </Grid>
      </Sheet>
      <CoursesTable sx={{ mt: 4 }} />
    </Box>
  );
}

export default CoursesPage;
