import { FormControl, InputLabel, MenuItem, Select } from '@mui/material';

const RightBar = () => {
  return (
    <div className='right-bar'>
      <FormControl fullWidth>
        <InputLabel id='demo-simple-select-label'>Age</InputLabel>
        <Select labelId='demo-simple-select-label' id='demo-simple-select' value={''} label='Age'>
          <MenuItem value={10}>Ten</MenuItem>
          <MenuItem value={20}>Twenty</MenuItem>
          <MenuItem value={30}>Thirty</MenuItem>
        </Select>
      </FormControl>
      <div className='sort-options'>
        <h4>Сортировка по:</h4>
        <select value={''}>
          <option value='all-courses'>Все курсы</option>
          <option value='new-courses'>Новые</option>
          <option value='in-progress'>В процессе</option>
          <option value='completed'>Завершенные</option>
        </select>
      </div>

      <div className='filter-options'>
        <h4>Фильтрация по</h4>

        <div className='filter-category'>
          <h5>категориям</h5>
          <select value={''}>
            <option value=''>Все категории</option>
            <option value='technology'>Английский</option>
            <option value='business'>Бизнес</option>
            <option value='design'>Программирование</option>
          </select>
        </div>

        <div className='filter-price-range'>
          <h5>Price Range</h5>
          <input type='number' value={''} min='0' />
          <input type='number' value={''} min='0' />
        </div>
      </div>
    </div>
  );
};

export default RightBar;
