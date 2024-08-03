import GlobalStyles from '@mui/joy/GlobalStyles';
import Avatar from '@mui/joy/Avatar';
import Box from '@mui/joy/Box';
import Divider from '@mui/joy/Divider';
import IconButton from '@mui/joy/IconButton';
import Input from '@mui/joy/Input';
import List from '@mui/joy/List';
import ListItem from '@mui/joy/ListItem';
import ListItemButton, { listItemButtonClasses } from '@mui/joy/ListItemButton';
import Typography from '@mui/joy/Typography';
import Sheet from '@mui/joy/Sheet';
import { IconSearch, IconHelp, IconSettings, IconLogout, IconUserScan } from '@tabler/icons-react';

import { sidebarItems } from './sidebarItems';
import { SidebarItem } from './SidebarItem';
import { closeSidebar } from '@/shared/lib';
import ColorSchemeToggle from '@/features/theme/ui/ColorSchemeToggle';

export default function Sidebar() {
  return (
    <Sheet
      className='Sidebar'
      sx={{
        position: { xs: 'fixed', md: 'sticky' },
        transform: {
          xs: 'translateX(calc(100% * (var(--SideNavigation-slideIn, 0) - 1)))',
          md: 'none',
        },
        transition: 'transform 0.4s, width 0.4s',
        zIndex: 10000,
        height: '100dvh',
        width: 'var(--Sidebar-width)',
        top: 0,
        p: 2,
        flexShrink: 0,
        display: 'flex',
        flexDirection: 'column',
        gap: 2,
        borderRight: '1px solid',
        borderColor: 'divider',
      }}
    >
      <GlobalStyles
        styles={(theme) => ({
          ':root': {
            '--Sidebar-width': '220px',
            [theme.breakpoints.up('lg')]: {
              '--Sidebar-width': '240px',
            },
          },
        })}
      />
      <Box
        className='Sidebar-overlay'
        sx={{
          position: 'fixed',
          zIndex: 9998,
          top: 0,
          left: 0,
          width: '100vw',
          height: '100vh',
          opacity: 'var(--SideNavigation-slideIn)',
          backgroundColor: 'var(--joy-palette-background-backdrop)',
          transition: 'opacity 0.4s',
          transform: {
            xs: 'translateX(calc(100% * (var(--SideNavigation-slideIn, 0) - 1) + var(--SideNavigation-slideIn, 0) * var(--Sidebar-width, 0px)))',
            lg: 'translateX(-100%)',
          },
        }}
        onClick={() => closeSidebar()}
      />
      <Box sx={{ display: 'flex', gap: 1, alignItems: 'center' }}>
        <IconButton variant='soft' color='primary' size='sm'>
          <IconUserScan />
        </IconButton>
        <Typography level='title-lg'>LuckyCourse</Typography>
        <ColorSchemeToggle sx={{ ml: 'auto' }} />
      </Box>
      <Input size='sm' startDecorator={<IconSearch />} placeholder='Search' />
      <Box
        sx={{
          minHeight: 0,
          overflow: 'hidden auto',
          flexGrow: 1,
          display: 'flex',
          flexDirection: 'column',
          [`& .${listItemButtonClasses.root}`]: {
            gap: 1.5,
          },
        }}
      >
        <List
          size='sm'
          sx={{
            gap: 1,
            '--List-nestedInsetStart': '30px',
            '--ListItem-radius': (theme) => theme.vars.radius.sm,
          }}
        >
          {sidebarItems.map((sidebar) => {
            return <SidebarItem key={sidebar.to} {...sidebar} />;
          })}
        </List>

        <List
          size='sm'
          sx={{
            mt: 'auto',
            flexGrow: 0,
            '--ListItem-radius': (theme) => theme.vars.radius.sm,
            '--List-gap': '8px',
            mb: 2,
          }}
        >
          <ListItem>
            <ListItemButton>
              <IconHelp />
              Поддержка
            </ListItemButton>
          </ListItem>
          <ListItem>
            <ListItemButton>
              <IconSettings />
              Настройки
            </ListItemButton>
          </ListItem>
        </List>
      </Box>
      <Divider />
      <Box sx={{ display: 'flex', gap: 1, alignItems: 'center' }}>
        <Avatar
          variant='outlined'
          size='sm'
          src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTfGtrAgOIg4722RdOT1PRNtcq0fXIjIzlPqQ&usqp=CAU'
        />
        <Box sx={{ minWidth: 0, flex: 1 }}>
          <Typography level='title-sm'>Админ</Typography>
          <Typography level='body-xs'>wg@support.com</Typography>
        </Box>
        <IconButton size='sm' variant='plain' color='neutral'>
          <IconLogout />
        </IconButton>
      </Box>
    </Sheet>
  );
}
