import { SidebarItemProps } from '@/layouts/MainLayout/Sidebar/SidebarItem';
import { IconCertificate2, IconUser } from '@tabler/icons-react';

export const sidebarItems: SidebarItemProps[] = [
  {
    label: 'Курсы',
    to: '/courses',
    icon: <IconCertificate2 />,
  },
  {
    label: 'Пользователи',
    to: '/users',
    icon: <IconUser />,
  },
];
