import { useParams } from 'react-router-dom';
import { useGetCourseByIdQuery } from '@/api/courseApi.ts';

interface CourseDetailPageProps {
    courseId: string
}

const CourseDetailPage = () => {
  const { courseId } = useParams();
  const { data, error, isLoading } = useGetCourseByIdQuery(courseId);

  if (isLoading) return <div>{'Загрузка...'}</div>;

  return (
    <div>
      <h1>{data?.title}</h1>
      <p>{data?.description}</p>
    </div>
  );
};

export default CourseDetailPage;