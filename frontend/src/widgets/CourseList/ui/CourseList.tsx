import CourseCard from '@/entities/CourseCard/CourseCard.tsx';
import ImgCourse from '@/shared/assets/img-course.jpg';

import styles from './CourseList.module.scss';

const CourseList = () => {
  return (
    <div className={styles.listWrapper}>
      {[...new Array(9)].map((_, index) => (
        <CourseCard
          key={index}
          title={'Эксрпесс-курс английского'}
          description={
            'Курс включает в себя интенсив на 3 месяца, за которые вы сможете выйти на уровень A2 с абсолютного НУЛЯ и заговорить на нем увернно'
          }
          imgPath={ImgCourse}
        />
      ))}
    </div>
  );
};

export default CourseList;
