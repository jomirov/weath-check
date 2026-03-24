import { Route, Routes } from 'react-router-dom'
import './App.css'
import PostHeaderLayout from './layouts/PostHeaderLayout.jsx'
import ContentLayout from './layouts/ContentLayout.jsx'
import PostHeaderForSearch from './pages/Home/PostHeaderForSearch.jsx'
import Home from './pages/Home/Home.jsx'
import Header from './components/Header/Header.jsx'
import Footer from './components/Footer/Footer.jsx'

function App() {

  return (
    <>
      <Header/>
      <Routes>
        <Route element={<PostHeaderLayout/>}>
          <Route path="/" element={<PostHeaderForSearch/>}/>
          <Route path="/map"/>
          <Route path="/contacts"/>
        </Route>
      </Routes>
      <Routes>
        <Route element={<ContentLayout/>}>
          <Route path="/" element={<Home/>}/>
        </Route>
      </Routes>
      <Footer/>
    </>
  )

}

export default App
