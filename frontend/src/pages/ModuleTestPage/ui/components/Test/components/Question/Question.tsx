import { Question as TQuestion } from '@root/dto';
import styles from '../../Test.module.scss';

export const Question: React.FC<{
  question: TQuestion;
  onAnswer: (questionId: number, answerId: number) => void;
  selectedAnswer: number | null;
  submitted: boolean;
}> = ({ question, onAnswer, selectedAnswer, submitted }) => {
  const handleAnswerSelect = (answerId: number) => {
    if (!submitted) {
      onAnswer(question.id, answerId);
    }
  };

  return (
    <div>
      <h3 className={styles.question}>{question.text}</h3>
      <ul>
        {question?.answers?.map((answer) => {
          const isSelected = selectedAnswer === answer.id;
          const isCorrect = answer.is_correct;
          return (
            <li
              key={answer.id}
              onClick={() => handleAnswerSelect(answer.id)}
              className={styles.answer}
              style={{
                cursor: 'pointer',
                border: submitted
                  ? isSelected
                    ? isCorrect
                      ? '1px solid #24c44c'
                      : '1px solid #FF3B30'
                    : 'transparent'
                  : isSelected
                    ? 'lightgrey'
                    : 'transparent',
                backgroundColor: submitted
                  ? isSelected
                    ? isCorrect
                      ? '#5bcb77'
                      : '#FFF1EC'
                    : 'transparent'
                  : isSelected
                    ? 'lightgrey'
                    : 'transparent',
              }}
            >
              {answer.text}
            </li>
          );
        })}
      </ul>
    </div>
  );
};
