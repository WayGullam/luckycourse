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

type CourseConstructorFormState = {
  title: string;
  description: string;
  img: string;
  modules: {
    id: number;
    title: string;
    description: string;
    lessons?: { id: number; title: string; description: string; content: string }[];
  }[];
};

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

const CourseConstructorPage = () => {
  const form = useForm({
    defaultValues,
  });

  return (
    <Box width='100%'>
      <PageTitle
        title='Конструктор курса'
        buttonText='Сохранить'
        ButtonProps={{ color: 'success', variant: 'soft' }}
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
        {form.watch('modules')?.map((module, moduleIndex) => (
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
            {module.lessons?.map((lesson, lessonIndex) => (
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
                </Grid>
              </Sheet>
            ))}
          </Sheet>
        ))}
      </Sheet>
    </Box>
  );
};

export default CourseConstructorPage;
