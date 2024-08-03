import { useParams } from 'react-router-dom';
import { useGetCourseByIdQuery } from '@/api/courseApi.ts';

import styles from './CoursePage.module.scss';
import { useState } from 'react';

const CoursePage = () => {
  const { courseId } = useParams();
  const serializedCourseId = parseInt(String(courseId));
  const { data, isLoading } = useGetCourseByIdQuery(serializedCourseId, {
    skip: Number.isNaN(serializedCourseId),
  });
  const [openModuleId, setOpenModuleId] = useState<number | null>(null);

  const handleOpenModule = (id: number) => {
    setOpenModuleId((prevId) => (prevId === id ? null : id));
  };

  if (isLoading) return <div>{'Загрузка...'}</div>;

  return (
    <div>
      <h1>{data?.title}</h1>
      <p>{data?.description}</p>
      <ul className={styles.modulesList}>
        {data?.modules.map((module) => (
          <li
            key={module.id}
            className={styles.moduleItem}
            onClick={() => handleOpenModule(module.id)}
          >
            {module.title}
            {openModuleId === module.id && (
              <ul className={styles.moduleLessons}>
                {module.lessons?.map((lesson) => (
                  <li key={lesson.id} className={styles.lessonItem}>
                    {lesson.content}
                  </li>
                ))}
              </ul>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default CoursePage;
