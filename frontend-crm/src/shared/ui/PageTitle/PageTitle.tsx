import { Box, Button, ButtonProps, Typography } from '@mui/joy';
import { IconPlus } from '@tabler/icons-react';

export type PageTitleProps = {
  title: string;
  onClick?: () => void;
  buttonText?: string;
  ButtonProps?: ButtonProps;
  plusIcon?: boolean;
};

export const PageTitle = ({
  title,
  onClick,
  buttonText = 'Создать',
  ButtonProps,
  plusIcon = false,
}: PageTitleProps) => {
  return (
    <Box
      sx={{ display: 'flex', width: '100%', justifyContent: 'space-between', alignItems: 'center' }}
    >
      <Typography level='h2' component='h2'>
        {title}
      </Typography>
      <Button
        fullWidth
        variant='outlined'
        onClick={onClick}
        {...ButtonProps}
        sx={{ maxWidth: 200 }}
      >
        <Box component='span' mr={0.5}>
          {buttonText}
        </Box>{' '}
        {plusIcon && <IconPlus size={16} style={{ flexShrink: 0 }} />}
      </Button>
    </Box>
  );
};
