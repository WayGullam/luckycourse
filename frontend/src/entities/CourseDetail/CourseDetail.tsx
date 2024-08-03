import { useParams } from 'react-router-dom';
import { useGetCourseByIdQuery } from '@/api/courseApi.ts';

const CourseDetail = () => {
  const { courseId } = useParams();

  const serializedCourseId = parseInt(String(courseId));
  const { data, error, isLoading } = useGetCourseByIdQuery(serializedCourseId, {
    skip: !Number.isNaN(serializedCourseId),
  });

  if (isLoading) return <div>{'Загрузка...'}</div>;

  return (
    <div>
      <h1>{data?.title}</h1>
      <p>{data?.description}</p>
    </div>
  );
};

export default CourseDetail;
