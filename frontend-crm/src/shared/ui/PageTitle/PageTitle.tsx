import { Box, Button, Typography } from '@mui/joy';
import { IconPlus } from '@tabler/icons-react';

export type PageTitleProps = {
  title: string;
};

export const PageTitle = ({ title }: PageTitleProps) => {
  return (
    <Box
      sx={{ display: 'flex', width: '100%', justifyContent: 'space-between', alignItems: 'center' }}
    >
      <Typography level='h2' component='h2'>
        {title}
      </Typography>
      <Button fullWidth variant='outlined' sx={{ maxWidth: 200 }}>
        <Box component='span' mr={0.5}>
          Создать
        </Box>{' '}
        <IconPlus size={16} style={{ flexShrink: 0 }} />
      </Button>
    </Box>
  );
};
