import { Test as TTest } from '@root/dto';
import { useState } from 'react';
import { Question } from './components/Question';
import styles from './Test.module.scss';
import { Button } from '@mui/material';

interface AnswersState {
  [key: number]: number;
}

export const Test = ({ test }: { test: TTest }) => {
  const [answers, setAnswers] = useState<AnswersState>({});
  const [submitted, setSubmitted] = useState(false);

  const handleAnswer = (questionId: number, answerId: number) => {
    console.log({ questionId, answerId }, 'Test component | handleAnswer');
    setAnswers({
      ...answers,
      [questionId]: answerId,
    });
  };

  const handleSubmit = () => {
    setSubmitted(true);
  };

  return (
    <div>
      <div className={styles.testWrapper}>
        <h2 className={styles.title}>{test.title}</h2>
        {test.questions.map((question) => (
          <Question
            key={question.id}
            question={question}
            onAnswer={handleAnswer}
            selectedAnswer={answers[question.id] || null}
            submitted={submitted}
          />
        ))}
        <Button onClick={handleSubmit} variant='outlined' style={{ marginTop: '10px' }}>
          Завершить тест
        </Button>
      </div>
    </div>
  );
};
