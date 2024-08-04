import { useLocation } from 'react-router-dom';
import { Typography, Box, Container, Paper } from '@mui/material';
import styles from './LessonPage.module.scss';

const LessonPage = () => {
  const location = useLocation();
  const lesson = location.state as {
    id: number;
    title: string;
    description: string;
    content: string;
  };

  if (!lesson) return <div>{'Урок не найден'}</div>;

  return (
    <Container maxWidth='md' className={styles.lessonContainer}>
      <Paper elevation={3} className={styles.lessonPaper}>
        <Box className={styles.lessonHeader}>
          <Typography variant='h2' className={styles.lessonTitle}>
            {lesson.title}
          </Typography>
          <img
            src='/path/to/illustration.png'
            alt='Illustration'
            className={styles.lessonIllustration}
          />
        </Box>
        <Typography variant='body1' className={styles.lessonDescription}>
          {lesson.description}
        </Typography>
        <div dangerouslySetInnerHTML={{ __html: lesson.content }} />
      </Paper>
    </Container>
  );
};

export default LessonPage;
