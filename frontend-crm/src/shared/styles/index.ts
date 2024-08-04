export const lineClampSx = (lines: number) => ({
  overflow: 'hidden',
  textOverflow: 'ellipsis',
  display: '-webkit-box',
  WebkitLineClamp: lines,
  lineClamp: lines,
  WebkitBoxOrient: 'vertical',
  boxOrient: 'vertical',
});

export const flexCenterSx = {
  display: 'flex',
  justifyContent: 'center',
  alignItems: 'center',
};
