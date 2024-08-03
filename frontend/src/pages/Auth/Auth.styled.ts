import { Box, Button, Paper, TextField } from '@mui/material';
import styled from 'styled-components';

export const FullHeightBox = styled(Box)`
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
`;

export const StyledFormContainer = styled(Paper)`
  padding: 24px;
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  max-width: 400px;
  box-shadow: 0px 3px 6px rgba(0, 0, 0, 0.16);
  border-radius: 12px;
`;

export const StyledTextField = styled(TextField)`
  & .MuiOutlinedInput-root {
    border-radius: 12px;
  }
`;

export const StyledButton = styled(Button)`
  margin-top: 24px;
  margin-bottom: 16px;
  background-color: #3f51b5;
  border-radius: 12px;
  &:hover {
    background-color: #303f9f;
  }
`;
