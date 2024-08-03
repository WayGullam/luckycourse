import CourseCard from '@/entities/CourseCard/CourseCard.tsx';

import styles from './CourseList.module.scss';
import { useGetCoursesQuery } from '@/api/courseApi';

const CourseList = () => {
  const coursesQuery = useGetCoursesQuery();

  return (
    <div className={styles.listWrapper}>
      {coursesQuery?.data?.map((course) => <CourseCard course={course} key={course.id} />)}
    </div>
  );
};

export default CourseList;
