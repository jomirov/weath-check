import { Route, Routes } from 'react-router-dom'
import './App.css'
import PostHeaderLayout from './layouts/PostHeaderLayout.jsx'
import ContentLayout from './layouts/ContentLayout.jsx'
import PostHeaderForSearch from './pages/Home/PostHeaderForSearch.jsx'
import Home from './pages/Home/Home.jsx'
import Header from './components/Header/Header.jsx'
import Footer from './components/Footer/Footer.jsx'
import { useState } from 'react'
import Map from './pages/Map/Mapp.jsx'
import Contacts from './pages/Contacts/Contacts.jsx'

function App() {

  const [ forecastMode, setForecastMode ] = useState(false);

  return (
    <>
      <Header/>
      <Routes>
        <Route element={<PostHeaderLayout/>}>
          <Route path="/" element={<PostHeaderForSearch setForecastMode={ setForecastMode }/>}/>
          <Route path="/map" element={<></>}/>
          <Route path="/contacts" element={<></>}/>
        </Route>
      </Routes>
      <Routes>
        <Route element={<ContentLayout/>}>
          <Route path="/" element={<Home forecastMode={ forecastMode }/>}/>
          <Route path="/map" element={<Map/>}/>
          <Route path="/contacts" element={<Contacts/>}/>
        </Route>
      </Routes>
      <Footer/>
    </>
  )

}

export default App
