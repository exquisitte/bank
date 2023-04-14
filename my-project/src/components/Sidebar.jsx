import React from 'react'
import './Sidebar.scss'
import Send from './img/icons8-отправлено-30 1.png'
import Plata from './img/icons8-сумка-с-евро-30 (1) 1.png'
import Profile from './img/icons8-мужчина-30 (1) 1.png'

const Sidebar = () => {
  return (
    <div className='sidebar'>
      <div className='block'>
        <div className="send">
            <img src={Send} alt="" />
            <span>Перекази</span>
        </div>
        <div className="plategi">
            <img src={Plata} alt="" />
            <span>Платежі</span>
        </div>
        <div className="profile">
          <img src={Profile} alt="" />
          <span>Мій профіль</span>
        </div>
      </div>
    </div>
  )
}

export default Sidebar
