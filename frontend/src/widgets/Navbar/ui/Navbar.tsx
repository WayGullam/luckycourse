import { AppLink } from 'shared/ui/AppLink/AppLink';
import cls from './Navbar.module.scss';
import clsx from 'clsx';
import Logo from '@/shared/assets/icons/logo.svg';

interface NavbarProps {
  className?: string;
}

export const Navbar = ({ className }: NavbarProps) => (
  <div className={clsx(cls.navbar, {}, [className])}>
    <div className={cls.wrapper}>
      <div>
        <img src={Logo} className={cls.logo} />
      </div>
      <div className={cls.links}>
        <AppLink to='/' className={cls.mainLink}>
          Перейти на главаную
        </AppLink>
        <AppLink to='/course'>Перейти на курс</AppLink>
      </div>
    </div>
  </div>
);
