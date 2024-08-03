import { useDeleteCourseMutation } from '@/api/courseApi';
import { CoursesTable } from '@/entities/course/ui/CoursesTable';
import { Collapse } from '@/shared/ui/Collapse';
import { PageTitle } from '@/shared/ui/PageTitle';
import {
  Box,
  Button,
  DialogActions,
  DialogContent,
  DialogTitle,
  Divider,
  Grid,
  Input,
  Modal,
  ModalDialog,
  Sheet,
} from '@mui/joy';
import { Course } from '@root/dto';
import { IconAlertTriangleFilled, IconSearch } from '@tabler/icons-react';
import { useBoolean } from 'ahooks';
import { useState } from 'react';

function CoursesPage() {
  const [filterOpen, filterOpenActions] = useBoolean();
  const [deleteModalOpen, deleteModalOpenActions] = useBoolean();
  const [course, setCourse] = useState<Course | null>(null);
  const [deleteCourse] = useDeleteCourseMutation();

  const deleteHandler = async () => {
    if (!course) return;

    try {
      await deleteCourse(course?.id).unwrap();
    } catch {
      console.log('error');
    } finally {
      deleteModalOpenActions.setFalse();
    }
  };

  return (
    <Box width='100%'>
      <PageTitle title='Курсы' />
      <Box mt={4} width={200}>
        <Button fullWidth variant='outlined' color='warning' onClick={filterOpenActions.toggle}>
          Фильтры
        </Button>
      </Box>
      <Collapse isOpen={filterOpen}>
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
              <Input
                placeholder='Поиск'
                sx={(theme) => ({ bgcolor: theme.palette.background.body })}
                startDecorator={<IconSearch />}
              />
            </Grid>
          </Grid>
        </Sheet>
      </Collapse>
      <CoursesTable
        sx={{ mt: 4 }}
        onDelete={(course) => {
          deleteModalOpenActions.setTrue();
          setCourse(course);
        }}
      />
      <Modal open={deleteModalOpen} onClose={deleteModalOpenActions.setFalse}>
        <ModalDialog variant='outlined' role='alertdialog'>
          <DialogTitle>
            <IconAlertTriangleFilled />
            Удалить курс?
          </DialogTitle>
          <Divider />
          <DialogContent>Вы действительно хотите удалить курс "{course?.title}"?</DialogContent>
          <DialogActions>
            <Button variant='solid' color='danger' onClick={() => deleteHandler()}>
              Удалить курс
            </Button>
            <Button variant='plain' color='neutral' onClick={deleteModalOpenActions.setFalse}>
              Отмена
            </Button>
          </DialogActions>
        </ModalDialog>
      </Modal>
    </Box>
  );
}

export default CoursesPage;
