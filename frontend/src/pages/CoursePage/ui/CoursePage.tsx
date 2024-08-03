import { useParams } from 'react-router-dom';
import { useGetCourseByIdQuery } from '@/api/courseApi.ts';


const CoursePage = () => {
  const { courseId } = useParams();
    console.log(courseId)
  const { data, error, isLoading } = useGetCourseByIdQuery(courseId);

  if (isLoading) return <div>{'Загрузка...'}</div>;

  return (
    <div>
      <h1>{data?.title}</h1>
      <p>{data?.description}</p>
    </div>
  );
};

export default CoursePage;
