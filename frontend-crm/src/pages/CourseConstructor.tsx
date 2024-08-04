import { PageTitle } from '@/shared/ui/PageTitle';
import { Box, FormControl, FormLabel, Grid, Input, Sheet, Textarea, Typography } from '@mui/joy';
import { Module } from '@root/dto';
import { useForm } from 'react-hook-form';
import ReactImagePickerEditor, { ImagePickerConf } from 'react-image-picker-editor';

type CourseConstructorFormState = {
  title: string;
  description: string;
  img: string;
  modules: Module[];
};

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
              <Textarea minRows={4} {...form.register('description')} />
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
        <Typography level='h4'>Модули</Typography>
      </Sheet>
    </Box>
  );
};

export default CourseConstructorPage;
