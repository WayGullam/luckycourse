import { Box, Button, Paper, TextField } from '@mui/material';
import styled from 'styled-components';

export const FullHeightBox = styled(Box)`
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
`;

export const StyledFormContainer = styled(Paper)`
  padding: 52px;
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  max-width: 600px;
  border-radius: 12px;
  background-color: rgba(255, 255, 255, 0.9);
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
  &:hover {
    background-color: #303f9f;
  }
`;
