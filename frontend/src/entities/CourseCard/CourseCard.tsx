import { Course } from '@root/dto.ts';
import ImgCourse from '@/shared/assets/img-course.jpg';

import styles from './CourseCard.module.scss';
import { AppLink } from '@/shared/ui/AppLink/AppLink.tsx';

interface IProps {
  course: Course;
}

const CourseCard = ({ course }: IProps) => {
  const { title, description, img_url } = course;

  return (
    <div className={styles.cardWrapper}>
      <AppLink to={`/courses/${course.id}`}>
        <div>
          <img src={img_url || ImgCourse} alt={title} />
        </div>
        <h1>{title}</h1>
        <p>{description}</p>
      </AppLink>
    </div>
  );
};

export default CourseCard;
