import {
  DialogContent,
  DialogTitle,
  Divider,
  Modal,
  ModalClose,
  ModalDialog,
  ModalProps,
} from '@mui/joy';
import { TestConstructor } from '../TestConstructor/TestConstructor';
import { CourseConstructorFormState } from '@/pages/CourseConstructor/types';
import { UseFormReturn } from 'react-hook-form';

export type TestConstructorModalProps = Omit<ModalProps, 'children'> & {
  form: UseFormReturn<CourseConstructorFormState>;
  moduleIndex: number;
};

export const TestConstructorModal = ({
  form,
  moduleIndex,
  ...props
}: TestConstructorModalProps) => {
  return (
    <Modal {...props}>
      <ModalDialog variant='outlined' maxWidth={900} sx={{ width: '100%' }}>
        <ModalClose />
        <DialogTitle>Создать тест</DialogTitle>
        <Divider />
        <DialogContent>
          <TestConstructor
            moduleIndex={moduleIndex}
            form={form}
            onSave={() => props.onClose?.({}, 'closeClick')}
          />
        </DialogContent>
      </ModalDialog>
    </Modal>
  );
};
