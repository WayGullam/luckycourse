import { TestConstructorModal } from '@/widgets/TestConstructorModal/TestConstructorModal';
import { Button } from '@mui/joy';
import { IconPlus } from '@tabler/icons-react';
import { UseFormReturn } from 'react-hook-form';
import { CourseConstructorFormState } from './types';
import { QuestionType } from '@root/dto';

type CreateTestConstructorBtnProps = {
  form: UseFormReturn<CourseConstructorFormState>;
  moduleIndex: number;
  open: boolean;
  setOpen: (bool: boolean) => void;
};
export const CreateTestConstructorBtn = ({
  form,
  moduleIndex,
  open: modalOpen,
  setOpen: setModalOpen,
}: CreateTestConstructorBtnProps) => {
  return (
    <>
      {!form.getValues(`modules.${moduleIndex}.test.questions`).length && (
        <Button
          variant='outlined'
          color='neutral'
          onClick={() => {
            if (!form.getValues(`modules.${moduleIndex}.test.questions`)?.length) {
              form.setValue(`modules.${moduleIndex}.test.questions`, [
                {
                  id: Date.now(),
                  text: '',
                  answers: [{ id: Date.now(), is_correct: false, text: '' }],
                  type: QuestionType.Single,
                },
              ]);
            }
            setModalOpen(true);
          }}
        >
          Добавить тест <IconPlus size={16} />
        </Button>
      )}
      <TestConstructorModal
        form={form}
        moduleIndex={moduleIndex}
        open={modalOpen}
        onClose={() => setModalOpen(false)}
      />
    </>
  );
};
