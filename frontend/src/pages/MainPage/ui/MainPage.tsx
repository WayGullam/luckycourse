import { useGetCoursesQuery } from '@/api/courseApi';
import CourseList from '@/widgets/CourseList/ui/CourseList.tsx';

const MainPage = () => {
  const coursesQuery = useGetCoursesQuery();

  console.log(coursesQuery.data);

  return (
    <div>
      <CourseList />
    </div>
  );
};

export default MainPage;
