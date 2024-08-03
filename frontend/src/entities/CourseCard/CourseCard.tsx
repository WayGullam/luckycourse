import { FC } from 'react';
import { Course } from '@root/dto.ts';

import styles from './CourseCard.module.scss';
import { AppLink } from '@/shared/ui/AppLink/AppLink.tsx';

const CourseCard: FC<Course> = (props) => {
  const { id, title, description, imgPath, modules, progress, status } = props;

  return (
    <div className={styles.cardWrapper}>
      <AppLink to={'/course'}>
        <div>
          <img src={imgPath} alt={title} />
        </div>
        <h1>{title}</h1>
        <p>{description}</p>
      </AppLink>
    </div>
  );
};

export default CourseCard;
