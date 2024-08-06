/* eslint-disable @typescript-eslint/no-explicit-any */
import { useDeleteUserMutation } from '@/api/userApi';
import { UsersTable } from '@/entities/user/ui/UsersTable/UsersTable';
import { PageTitle } from '@/shared/ui/PageTitle';
import {
  Box,
  Button,
  DialogActions,
  DialogContent,
  DialogTitle,
  Divider,
  Modal,
  ModalDialog,
} from '@mui/joy';
import { IconAlertTriangleFilled } from '@tabler/icons-react';
import { useBoolean } from 'ahooks';
import { useState } from 'react';

const UsersPage = () => {
  const [deleteModalOpen, deleteModalOpenActions] = useBoolean();
  const [user, setUser] = useState<any>(null);
  const [deleteUser] = useDeleteUserMutation();

  const deleteHandler = async () => {
    if (!user) return;

    try {
      await deleteUser(user?.id).unwrap();
    } catch {
      console.log('error');
    } finally {
      deleteModalOpenActions.setFalse();
    }
  };

  return (
    <Box width='100%'>
      <PageTitle hideBtn title='Пользователи' />
      <Box mt={2}>
        <UsersTable
          onDelete={(user) => {
            deleteModalOpenActions.setTrue();
            setUser(user);
          }}
        />
      </Box>
      <Modal open={deleteModalOpen} onClose={deleteModalOpenActions.setFalse}>
        <ModalDialog variant='outlined' role='alertdialog'>
          <DialogTitle>
            <IconAlertTriangleFilled />
            Удалить пользователя?
          </DialogTitle>
          <Divider />
          <DialogContent>
            Вы действительно хотите удалить пользователя с id "{user?.id}"?
          </DialogContent>
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
};

export default UsersPage;
