import { flexCenterSx } from '@/shared/styles';
import { CKEditor } from '@/shared/ui/CKEditor/CKEditor';
import { PageTitle } from '@/shared/ui/PageTitle';
import {
  Box,
  Button,
  FormControl,
  FormLabel,
  Grid,
  IconButton,
  Input,
  Sheet,
  Textarea,
  Typography,
} from '@mui/joy';
import { IconPlus, IconTrash } from '@tabler/icons-react';
import { useForm } from 'react-hook-form';
import ReactImagePickerEditor, { ImagePickerConf } from 'react-image-picker-editor';
import { CourseConstructorFormState } from './types';
import { useCreateCourseMutation } from '@/api/courseApi';
import { serizalizeCourseConstructorFormState } from './lib';
import { toast } from 'react-toastify';
import { CreateTestConstructorBtn } from './CreateTestConstructorBtn';

const generateNewLesson = () => ({
  id: Date.now(),
  title: '',
  description: '',
  content: '',
});

const generateNewModule = () => ({
  id: Date.now(),
  title: '',
  description: '',
  lessons: [],
  test: [],
});

const defaultValues: CourseConstructorFormState = {
  title: '',
  description: '',
  img: '',
  modules: [],
};

const imagePickerConfig: ImagePickerConf = {
  borderRadius: '8px',
  language: 'ru',
  width: '300px',
  aspectRatio: 4 / 3,
  objectFit: 'cover',
  compressInitial: null,
  hideDownloadBtn: true,
};

export const CourseConstructorPage = () => {
  const form = useForm({
    defaultValues,
  });
  const [createCourse] = useCreateCourseMutation();

  const createHandler = async () => {
    try {
      await createCourse(serizalizeCourseConstructorFormState(form.getValues())).unwrap();
      toast.success('Курс создан');
    } catch {
      toast.error('Ошибка!');
    }
  };

  return (
    <Box width='100%'>
      <PageTitle
        title='Конструктор курса'
        buttonText='Сохранить'
        ButtonProps={{ color: 'success', variant: 'soft' }}
        onClick={() => createHandler()}
      />
      <Sheet sx={(theme) => ({ borderRadius: theme.radius.sm, padding: 2, mt: 6 })}>
        <Typography level='h4'>Основная информация</Typography>
        <Grid container spacing={2} mt={2}>
          <Grid xs={12}>
            <FormControl>
              <FormLabel>Название</FormLabel>
              <Input {...form.register('title')} />
            </FormControl>
          </Grid>

          <Grid xs={12} md={6}>
            <FormControl>
              <FormLabel>Описание</FormLabel>
              <Textarea minRows={9} {...form.register('description')} />
            </FormControl>
          </Grid>
          <Grid xs={12} md={6}>
            <Box
              sx={(theme) => ({
                maxWidth: 500,
                margin: '0 auto',
                '& .popup': {
                  [theme.breakpoints.up('md')]: {
                    width: 'calc(100dvw - var(--Sidebar-width))',
                    marginLeft: 'var(--Sidebar-width)',
                  },
                  [theme.breakpoints.down('lg')]: {
                    marginTop: 'var(--Header-height)',
                  },
                },
              })}
            >
              <FormControl>
                <FormLabel>Картинка</FormLabel>
                <ReactImagePickerEditor
                  config={imagePickerConfig}
                  imageSrcProp={form.watch('img')}
                  imageChanged={(img: string) => form.setValue('img', img)}
                />
              </FormControl>
            </Box>
          </Grid>
        </Grid>
      </Sheet>
      <Sheet sx={(theme) => ({ borderRadius: theme.radius.sm, padding: 2, mt: 6 })}>
        <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <Typography level='h4'>Модули</Typography>
          <Button
            variant='outlined'
            onClick={() =>
              form.setValue('modules', [...form.watch('modules'), generateNewModule()])
            }
          >
            Добавить модуль <IconPlus size={16} />
          </Button>
        </Box>
        {form.watch('modules')?.map((module, moduleIndex, modules) => (
          <Sheet
            key={module.id}
            sx={(theme) => ({
              bgcolor: theme.palette.background.level1,
              borderRadius: theme.radius.sm,
              padding: 2,
              mt: 2,
            })}
          >
            <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <Typography component='p' level='title-md'>
                Модуль {moduleIndex + 1}.
              </Typography>
              <IconButton
                onClick={() => {
                  form.setValue(
                    'modules',
                    form.getValues().modules.filter((m) => m.id !== module.id),
                  );
                }}
                color='danger'
              >
                <IconTrash />
              </IconButton>
            </Box>
            <Grid container spacing={2} mt={1}>
              <Grid xs={12} md={6}>
                <FormControl>
                  <FormLabel>Название</FormLabel>
                  <Input {...form.register(`modules.${moduleIndex}.title`)} />
                </FormControl>
              </Grid>
              <Grid xs={12} md={6}>
                <FormControl>
                  <FormLabel>Описание</FormLabel>
                  <Textarea {...form.register(`modules.${moduleIndex}.description`)} />
                </FormControl>
              </Grid>
            </Grid>
            <Box
              sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mt: 2 }}
            >
              <Typography component='p' level='title-md'>
                Уроки
              </Typography>
              <Button
                variant='outlined'
                onClick={() =>
                  form.setValue(`modules.${moduleIndex}.lessons`, [
                    ...(form.watch(`modules.${moduleIndex}.lessons`) || []),
                    generateNewLesson(),
                  ])
                }
              >
                Добавить урок <IconPlus size={16} />
              </Button>
            </Box>
            {module.lessons?.map((lesson, lessonIndex, lessons) => (
              <Sheet
                key={lesson.id}
                sx={(theme) => ({
                  bgcolor: theme.palette.background.level2,
                  borderRadius: theme.radius.sm,
                  padding: 2,
                  mt: 2,
                })}
              >
                <Box
                  sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}
                >
                  <Typography component='p' level='title-md'>
                    Урок {lessonIndex + 1}.
                  </Typography>
                  <IconButton
                    onClick={() => {
                      form.setValue(
                        `modules.${moduleIndex}.lessons`,
                        (form.watch(`modules.${moduleIndex}.lessons`) || []).filter(
                          (l) => l.id !== lesson.id,
                        ),
                      );
                    }}
                    color='danger'
                  >
                    <IconTrash />
                  </IconButton>
                </Box>
                <Grid container spacing={2}>
                  <Grid xs={12} md={6}>
                    <FormControl>
                      <FormLabel>Название</FormLabel>
                      <Input
                        {...form.register(`modules.${moduleIndex}.lessons.${lessonIndex}.title`)}
                      />
                    </FormControl>
                  </Grid>
                  <Grid xs={12} md={6}>
                    <FormControl>
                      <FormLabel>Описание</FormLabel>
                      <Textarea
                        {...form.register(
                          `modules.${moduleIndex}.lessons.${lessonIndex}.description`,
                        )}
                      />
                    </FormControl>
                  </Grid>
                  <Grid xs={12}>
                    <FormControl>
                      <FormLabel>Контент</FormLabel>
                      <CKEditor
                        data={lesson.content}
                        onChange={(_, editor) => {
                          form.setValue(
                            `modules.${moduleIndex}.lessons.${lessonIndex}.content`,
                            editor.getData(),
                          );
                        }}
                      />
                    </FormControl>
                  </Grid>
                </Grid>
                {lesson.title && lessons.length === lessonIndex + 1 && (
                  <Box mt={2} sx={flexCenterSx}>
                    <Button
                      variant='outlined'
                      onClick={() =>
                        form.setValue(`modules.${moduleIndex}.lessons`, [
                          ...(form.watch(`modules.${moduleIndex}.lessons`) || []),
                          generateNewLesson(),
                        ])
                      }
                    >
                      Добавить урок <IconPlus size={16} />
                    </Button>
                  </Box>
                )}
              </Sheet>
            ))}
            {!!module.lessons?.length && modules.length === moduleIndex + 1 && (
              <Box mt={2} sx={[flexCenterSx, { columnGap: 2 }]}>
                <Button
                  variant='outlined'
                  onClick={() =>
                    form.setValue('modules', [...form.watch('modules'), generateNewModule()])
                  }
                >
                  Добавить модуль <IconPlus size={16} />
                </Button>
                <CreateTestConstructorBtn form={form} moduleIndex={moduleIndex} />
              </Box>
            )}
          </Sheet>
        ))}
      </Sheet>
    </Box>
  );
};

export default CourseConstructorPage;
