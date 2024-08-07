import { useParams, useNavigate } from 'react-router-dom';
import { useGetCourseByIdQuery } from '@/api/courseApi.ts';
import { IoIosArrowDown, IoIosArrowUp } from 'react-icons/io';
import styles from './CoursePage.module.scss';
import { useState } from 'react';
import { Test } from '@root/dto';

const CoursePage = () => {
  const { courseId } = useParams();
  const navigate = useNavigate();
  const serializedCourseId = parseInt(String(courseId));
  const { data, isLoading } = useGetCourseByIdQuery(serializedCourseId, {
    skip: Number.isNaN(serializedCourseId),
  });
  const [openModuleId, setOpenModuleId] = useState<number | null>(null);

  const handleOpenModule = (id: number) => {
    setOpenModuleId((prevId) => (prevId === id ? null : id));
  };

  const handleLessonClick = (lesson: {
    id: number;
    title: string;
    description: string;
    content: string;
  }) => {
    navigate(`/courses/${serializedCourseId}/lessons/${lesson.id}`, { state: lesson });
  };

  const handleLessonTest = (test: Test) => {
    navigate(`/courses/${serializedCourseId}/test/${test.id}`, { state: test });
  };

  if (isLoading) return <div>{'Загрузка...'}</div>;

  return (
    <div className={styles.fullCourseWrapper}>
      <div className={styles.courseInfo}>
        <div className={styles.courseTextInfo}>
          <h1>{data?.title}</h1>
          <p>{data?.description}</p>
        </div>
        <div className={styles.imgCourse}>
          <img src={data?.img_url} alt={data?.title} />
        </div>
      </div>
      <div className={styles.modules}>
        <h2 className={styles.mudulesTitle}>Модули курса</h2>
        <ul className={styles.modulesList}>
          {data?.modules.map((module) => (
            <div key={module.id}>
              <li className={styles.moduleItem} onClick={() => handleOpenModule(module.id)}>
                <div className={styles.moduleListTitle}>
                  <h2>{module.title}</h2>
                  {openModuleId === module.id ? <IoIosArrowUp /> : <IoIosArrowDown />}
                </div>
                {openModuleId === module.id && (
                  <ul className={styles.moduleLessons}>
                    {module.lessons?.map((lesson) => (
                      <li
                        key={lesson.id}
                        className={styles.lessonItem}
                        onClick={() => handleLessonClick(lesson)}
                      >
                        <h1>{lesson.title}</h1>
                      </li>
                    ))}
                    {module.test && (
                      <li
                        className={styles.lessonItem}
                        onClick={() => handleLessonTest(module.test)}
                      >
                        <h1>{module.test.title}</h1>
                      </li>
                    )}
                  </ul>
                )}
              </li>
            </div>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default CoursePage;
