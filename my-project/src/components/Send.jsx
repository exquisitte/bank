import React, { useState } from 'react';
import './Send.scss';

const Send = () => {
  const [number, setNumber] = useState('');

  const handleNumberChange = (event) => {
    const input = event.target.value.replace(/\s/g, '').slice(0, 16);
    setNumber(input);
  };

  const formatNumber = (number) => {
    // Добавляем пробел после каждых 4 символов
    return number.replace(/(\d{4})/g, '$1 ').trim();
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log(number);
  };

  return (
    <div className='Send'>
      <span>Переказ на карту</span>
      <div className='pole'>
          <input
            type='text'
            value={formatNumber(number)}
            onChange={handleNumberChange}
            placeholder='0000 0000 0000 0000'
            style={{
              letterSpacing: '0',
              padding: '10px 14px',
            }}
          />    
        <button className='btn' onClick={handleSubmit}>
          Отправить
        </button>
      </div>
    </div>
  );
};

export default Send;
