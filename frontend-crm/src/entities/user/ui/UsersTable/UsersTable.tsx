/* eslint-disable @typescript-eslint/no-explicit-any */
import {} from '@/api/courseApi';
import { useGetUsersQuery } from '@/api/userApi';
import { Box, BoxProps, Dropdown, IconButton, Menu, MenuButton, MenuItem, Table } from '@mui/joy';
import { Course } from '@root/dto';
import { IconDotsVertical } from '@tabler/icons-react';

export type UsersTableProps = BoxProps & {
  onDelete?: (course: Course) => void;
  onUserClick?: (course: Course) => void;
};

export const UsersTable = ({ sx, onDelete, onUserClick, ...props }: UsersTableProps) => {
  const usersQuery = useGetUsersQuery();
  const users = usersQuery.data;

  return (
    <Box sx={[{ width: '100%' }, ...(Array.isArray(sx) ? sx : [sx])]} {...props}>
      <Table hoverRow aria-label='courses list table' variant='plain' borderAxis='xBetween'>
        <thead>
          <tr>
            <th style={{ width: '40%' }}>ID</th>
            <th>ФИО</th>
            <th style={{ textAlign: 'right' }}>Действие</th>
          </tr>
        </thead>
        <tbody>
          {users?.map((user: any) => {
            return (
              <tr
                role='button'
                onClick={() => onUserClick?.(user)}
                key={user.id}
                style={{ cursor: 'pointer' }}
              >
                <td>{user.id}</td>
                <td>
                  {user?.user.first_name} {user?.user.last_name}
                </td>

                <td style={{ textAlign: 'right' }}>
                  <Dropdown>
                    <MenuButton
                      onClick={(e) => e.stopPropagation()}
                      component={IconButton}
                      sx={{ border: 'none' }}
                    >
                      <IconDotsVertical />
                    </MenuButton>
                    <Menu placement='bottom-end' variant='plain'>
                      <MenuItem
                        color='primary'
                        onClick={(e) => {
                          e.stopPropagation();
                        }}
                      >
                        Изменить
                      </MenuItem>
                      <MenuItem
                        color='danger'
                        onClick={(e) => {
                          e.stopPropagation();
                          onDelete?.(user);
                        }}
                      >
                        Удалить
                      </MenuItem>
                    </Menu>
                  </Dropdown>
                </td>
              </tr>
            );
          })}
        </tbody>
      </Table>
    </Box>
  );
};
