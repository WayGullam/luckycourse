import { Box } from '@mui/joy';
import { useRef, useEffect, HTMLAttributes } from 'react';

export type CollapseProps = HTMLAttributes<HTMLDivElement> & {
  isOpen?: boolean;
};

export const Collapse = ({ isOpen = false, children, ...props }: CollapseProps) => {
  const contentRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!contentRef.current) {
      return;
    }
    if (isOpen) {
      contentRef.current.style.height = `${contentRef.current.scrollHeight}px`;
      setTimeout(() => {
        if (contentRef.current) {
          contentRef.current.style.height = 'auto';
        }
      }, 300);
    } else {
      contentRef.current.style.height = `${contentRef.current.scrollHeight}px`;
      requestAnimationFrame(() => {
        if (contentRef.current) {
          contentRef.current.style.height = '0px';
        }
      });
    }
  }, [isOpen]);

  return (
    <Box
      ref={contentRef}
      sx={{ height: 0, overflow: 'hidden', transition: 'height 300ms linear' }}
      {...props}
    >
      {children}
    </Box>
  );
};
