import { useGetCoursesQuery } from '@/api/courseApi';
import { lineClampSx } from '@/shared/styles';
import { Box, BoxProps, Dropdown, IconButton, Menu, MenuButton, MenuItem, Table } from '@mui/joy';
import { Course } from '@root/dto';
import { IconDotsVertical } from '@tabler/icons-react';

export type CoursesTableProps = BoxProps & {
  onDelete?: (course: Course) => void;
};

export const CoursesTable = ({ sx, onDelete, ...props }: CoursesTableProps) => {
  const coursesQuery = useGetCoursesQuery();
  const courses = coursesQuery.data;

  return (
    <Box sx={[{ width: '100%' }, ...(Array.isArray(sx) ? sx : [sx])]} {...props}>
      <Table hoverRow aria-label='courses list table' variant='plain' borderAxis='xBetween'>
        <thead>
          <tr>
            <th style={{ width: '40%' }}>Название</th>
            <th>Описание</th>
            <th style={{ textAlign: 'right' }}>Модули</th>
            <th style={{ textAlign: 'right' }}>Действие</th>
          </tr>
        </thead>
        <tbody>
          {courses?.map((course) => {
            return (
              <tr key={course.id} style={{ cursor: 'pointer' }}>
                <td>{course.title}</td>
                <td>
                  <Box sx={lineClampSx(2)}>{course.description}</Box>
                </td>
                <td style={{ textAlign: 'right' }}>{course.modules?.length || 0}</td>
                <td style={{ textAlign: 'right' }}>
                  <Dropdown>
                    <MenuButton component={IconButton} sx={{ border: 'none' }}>
                      <IconDotsVertical />
                    </MenuButton>
                    <Menu placement='bottom-end' variant='plain'>
                      <MenuItem color='primary'>Изменить</MenuItem>
                      <MenuItem color='danger' onClick={() => onDelete?.(course)}>
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
