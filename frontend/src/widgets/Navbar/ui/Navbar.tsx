import { AppLink } from 'shared/ui/AppLink/AppLink';
import cls from './Navbar.module.scss';
import clsx from 'clsx';
import Logo from '@/shared/assets/icons/logo.svg';
import { useDispatch, useSelector } from 'react-redux';
import { logout, selectIsAuthenticated } from '@/entities/session/sessionSlice';

interface NavbarProps {
  className?: string;
}

export const Navbar = ({ className }: NavbarProps) => {
  const isAuthenticated = useSelector(selectIsAuthenticated);
  const dispatch = useDispatch();

  return (
    <div className={clsx(cls.navbar, {}, [className])}>
      <div className={cls.wrapper}>
        <AppLink to='/'>
          <img src={Logo} className={cls.logo} />
        </AppLink>
        {!isAuthenticated ? (
          <div className={cls.links}>
            <AppLink to='/auth' className={cls.mainLink}>
              Вход
            </AppLink>
            <AppLink to='/registration'>Регистрация</AppLink>
          </div>
        ) : (
          <button style={{ background: 'transparent' }} onClick={() => dispatch(logout())}>
            Выйти
          </button>
        )}
      </div>
    </div>
  );
};
