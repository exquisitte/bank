import React from 'react'
import './header.scss'
import Logo from './img/Vector 1.png'
import Search from './img/icons8-поиск-30 2.png'

const Header = () => {
  return (
    <header>
      <div className="search">
      <img src={Search} alt="" />
      </div>
      <div className="logo">
      <img src={Logo} alt="" />
    </div>
    </header>
  )
}

export default Header
