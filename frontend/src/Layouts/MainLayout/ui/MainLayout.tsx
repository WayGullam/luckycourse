import * as Styled from './MainLayout.styled';

interface IProps {
  children: React.ReactNode;
}

export const MainLayout = ({ children }: IProps) => {
  return <Styled.Root>{children}</Styled.Root>;
};
