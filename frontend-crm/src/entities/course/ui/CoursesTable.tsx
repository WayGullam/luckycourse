import { Box, BoxProps, Dropdown, IconButton, Menu, MenuButton, MenuItem, Table } from '@mui/joy';
import { IconDotsVertical } from '@tabler/icons-react';

export type CoursesTableProps = BoxProps;

export const CoursesTable = ({ sx, ...props }: CoursesTableProps) => {
  return (
    <Box sx={[{ width: '100%' }, ...(Array.isArray(sx) ? sx : [sx])]} {...props}>
      <Table hoverRow aria-label='courses list table' variant='plain' borderAxis='xBetween'>
        <thead>
          <tr>
            <th style={{ width: '40%' }}>Название</th>
            <th style={{ textAlign: 'right' }}>Описание</th>
            <th style={{ textAlign: 'right' }}>Модули</th>
            <th style={{ textAlign: 'right' }}>Действие</th>
          </tr>
        </thead>
        <tbody>
          <tr style={{ cursor: 'pointer' }}>
            <td>Frozen yoghurt</td>
            <td style={{ textAlign: 'right' }}>159</td>
            <td style={{ textAlign: 'right' }}>6</td>
            <td style={{ textAlign: 'right' }}>
              <Dropdown>
                <MenuButton component={IconButton} sx={{ border: 'none' }}>
                  <IconDotsVertical />
                </MenuButton>
                <Menu placement='bottom-end' variant='plain'>
                  <MenuItem color='primary'>Изменить</MenuItem>
                  <MenuItem color='danger'>Удалить</MenuItem>
                </Menu>
              </Dropdown>
            </td>
          </tr>
        </tbody>
      </Table>
    </Box>
  );
};
