import { TestConstructorModal } from '@/widgets/TestConstructorModal/TestConstructorModal';
import { Button } from '@mui/joy';
import { IconPlus } from '@tabler/icons-react';
import { useBoolean } from 'ahooks';
import { UseFormReturn } from 'react-hook-form';
import { CourseConstructorFormState } from './types';
import { QuestionType } from '@root/dto';

type CreateTestConstructorBtnProps = {
  form: UseFormReturn<CourseConstructorFormState>;
  moduleIndex: number;
};
export const CreateTestConstructorBtn = ({ form, moduleIndex }: CreateTestConstructorBtnProps) => {
  const [modalOpen, modalOpenActions] = useBoolean();

  return (
    <>
      <Button
        variant='outlined'
        color='neutral'
        onClick={() => {
          if (!form.getValues(`modules.${moduleIndex}.test`)?.length) {
            form.setValue(`modules.${moduleIndex}.test`, [
              {
                id: Date.now(),
                text: '',
                answers: [{ id: Date.now() }],
                type: QuestionType.Single,
              },
            ]);
          }
          modalOpenActions.setTrue();
        }}
      >
        Добавить тест <IconPlus size={16} />
      </Button>
      <TestConstructorModal
        form={form}
        moduleIndex={moduleIndex}
        open={modalOpen}
        onClose={modalOpenActions.setFalse}
      />
    </>
  );
};
