import { ListItem, ListItemButton, ListItemContent, Typography } from '@mui/joy';
import { ReactNode } from 'react';
import { useNavigate, useMatch } from 'react-router-dom';

export type SidebarItemProps = {
  icon: ReactNode;
  label: string;
  to: string;
};

export const SidebarItem = ({ icon, label, to }: SidebarItemProps) => {
  const match = useMatch(to);
  const navigate = useNavigate();

  return (
    <ListItem>
      <ListItemButton selected={!!match} onClick={() => navigate(to)}>
        {icon}
        <ListItemContent>
          <Typography level='title-sm'>{label}</Typography>
        </ListItemContent>
      </ListItemButton>
    </ListItem>
  );
};
