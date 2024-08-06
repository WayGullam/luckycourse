import { CourseConstructorFormState } from '@/pages/CourseConstructor/types';
import {
  Box,
  Button,
  Checkbox,
  FormControl,
  FormLabel,
  Grid,
  Input,
  Radio,
  RadioGroup,
  Typography,
} from '@mui/joy';
import { QuestionType } from '@root/dto';
import { IconPlus } from '@tabler/icons-react';
import React from 'react';
import { UseFormReturn } from 'react-hook-form';

export type TestConstructorProps = {
  form: UseFormReturn<CourseConstructorFormState>;
  moduleIndex: number;
  onSave?: () => void;
};

export const TestConstructor = ({ form, moduleIndex, onSave }: TestConstructorProps) => {
  return (
    <Box width='100%'>
      <Grid container spacing={2}>
        <Grid xs={12} md={6}>
          <FormControl>
            <FormLabel>Название</FormLabel>
            <Input {...form.register(`modules.${moduleIndex}.test.title`)} />
          </FormControl>
        </Grid>
        <Grid xs={12} md={6}>
          <FormControl>
            <FormLabel>Описание</FormLabel>
            <Input {...form.register(`modules.${moduleIndex}.test.description`)} />
          </FormControl>
        </Grid>
      </Grid>
      {form.watch(`modules.${moduleIndex}.test.questions`)?.map((question, questionIndex) => {
        return (
          <React.Fragment key={question.id}>
            <Grid container mt={2}>
              <Grid xs={12}>
                <FormControl>
                  <FormLabel>Вопрос {questionIndex + 1}</FormLabel>
                  <Input
                    placeholder={`Вопрос ${questionIndex + 1}`}
                    {...form.register(
                      `modules.${moduleIndex}.test.questions.${questionIndex}.text`,
                    )}
                  />
                </FormControl>
              </Grid>
            </Grid>
            <Box mt={2}>
              <Box sx={{ display: 'flex', gap: 2 }}>
                <Typography level='title-sm'>Тип ответа:</Typography>
                <RadioGroup
                  orientation='horizontal'
                  aria-labelledby='segmented-controls-example'
                  color='primary'
                  onChange={(e) =>
                    form.setValue(
                      `modules.${moduleIndex}.test.questions.${questionIndex}.type`,
                      parseInt(e.target.value),
                    )
                  }
                  value={form.watch(`modules.${moduleIndex}.test.questions.${questionIndex}.type`)}
                >
                  <Radio label='Одиночный выбор' value={QuestionType.Single} />
                  <Radio label='Множественный выбор' value={QuestionType.Multiple} />
                  <Radio label='Ввод' value={QuestionType.Input} />
                </RadioGroup>
              </Box>
              {question.type !== QuestionType.Input && (
                <>
                  <Typography level='title-sm' mt={2} mb={1}>
                    Варианты ответов:
                  </Typography>
                  <Box sx={{ display: 'flex', gap: 1, flexDirection: 'column' }}>
                    {question.answers.map((answer, answerIndex) => (
                      <Input
                        key={answer.id}
                        placeholder='Вариант ответа'
                        sx={{
                          overflow: 'hidden',
                          paddingLeft: '30px',
                        }}
                        endDecorator={
                          <Checkbox
                            variant='soft'
                            color='success'
                            onChange={(e) => {
                              const answersKey =
                                `modules.${moduleIndex}.test.questions.${questionIndex}.answers` as const;
                              if (question.type === QuestionType.Single) {
                                form.setValue(
                                  answersKey,
                                  form
                                    .getValues(answersKey)
                                    .map((item) => ({ ...item, is_correct: false })),
                                );
                              }
                              form.setValue(
                                `${answersKey}.${answerIndex}.is_correct`,
                                e.target.checked,
                              );
                            }}
                            checked={form.watch(
                              `modules.${moduleIndex}.test.questions.${questionIndex}.answers.${answerIndex}.is_correct`,
                            )}
                          />
                        }
                        {...form.register(
                          `modules.${moduleIndex}.test.questions.${questionIndex}.answers.${answerIndex}.text`,
                        )}
                        startDecorator={
                          <Box
                            sx={(theme) => ({
                              bgcolor: theme.palette.primary.softBg,
                              color: theme.palette.primary.solidColor,
                              position: 'absolute',
                              height: '100%',
                              width: 30,
                              left: 0,
                              top: 0,
                              display: 'flex',
                              alignItems: 'center',
                              justifyContent: 'center',
                            })}
                          >
                            <Typography level='title-md' textAlign='center'>
                              {answerIndex + 1}
                            </Typography>
                          </Box>
                        }
                      />
                    ))}
                  </Box>
                </>
              )}
            </Box>
            {question.type !== QuestionType.Input && (
              <Button
                sx={{ mt: 2 }}
                variant='soft'
                onClick={() => {
                  const key =
                    `modules.${moduleIndex}.test.questions.${questionIndex}.answers` as const;
                  form.setValue(key, [
                    ...form.getValues(key),
                    { id: Date.now(), text: '', is_correct: false },
                  ]);
                }}
              >
                Добавить вариант ответа <IconPlus size={16} />
              </Button>
            )}
          </React.Fragment>
        );
      })}
      <Box
        sx={[
          {
            flexWrap: 'wrap',
            justifyContent: 'flex-end',
            display: 'flex',
            gap: 1,
            alignItems: 'center',
            mt: 1,
          },
        ]}
      >
        <Button
          sx={{ mt: 1, display: 'flex' }}
          variant='outlined'
          onClick={() => {
            const key = `modules.${moduleIndex}.test.questions` as const;
            form.setValue(key, [
              ...form.getValues(key),
              {
                id: Date.now(),
                text: '',
                answers: [{ id: Date.now(), is_correct: false, text: '' }],
                type: QuestionType.Single,
              },
            ]);
          }}
        >
          Добавить вопрос <IconPlus size={16} />
        </Button>
        <Button
          sx={{ mt: 1, display: 'block', width: 150 }}
          variant='outlined'
          color='success'
          onClick={onSave}
        >
          Сохранить
        </Button>
      </Box>
    </Box>
  );
};
