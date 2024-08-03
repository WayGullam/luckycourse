import { FC } from 'react';
import { Link, LinkProps } from 'react-router-dom';
import cls from './AppLink.module.scss';
import clsx from 'clsx';

interface AppLinkProps extends LinkProps {
  className?: string;
}

export const AppLink: FC<AppLinkProps> = (props) => {
  const { to, className, children, ...otherProps } = props;

  return (
    <Link to={to} className={clsx(cls.AppLink, {}, [className])} {...otherProps}>
      {children}
    </Link>
  );
};
