import { useState, useEffect } from 'react';
import coverImg from './image/coverImg.png';
import './BoxOf.css';
import quote1 from './image/icon_up1.png';
import quote2 from './image/icon_up1.png';
import quote3 from './image/icon_up1.png';
import quote4 from './image/coverImg.png';



function BoxofEn(){
  const DATA = [quote1, quote2, quote3, quote4];
  const [visible, setVisible] = useState(true);
  const removeElement = () => {
  setVisible((prev) => !prev); };
  //const [random, setRandom] = useState('https://64.media.tumblr.com/27939018ad44f1840a7af7e9d07746a6/tumblr_pmw2z728IN1uvsi7jo3_1280.gifv');
  /*
  function randomClick() {
    const randomImg =  quoteAll.map[Math.floor(Math.random() * 5)]
    console.log(randomImg)  
    setRandom(randomImg)
        }
  */

  //const [randomData, setRandomData] = useState(() => getRandomObject(DATA));
  const getRandomObject = (array) => {
    const randomObject = array[Math.floor(Math.random() * array.length)];
    return randomObject;
  };
  
  const [randomData, setRandomData] = useState('https://i.pinimg.com/originals/52/86/71/528671b25753cd9e4f5e48c1586ae88b.gif');

  return (
    <div className="containBox">
      {visible && (
        <div className="cover">
          <img src={coverImg} alt=""/>
          <button className="btn_remove" onClick={removeElement}>Remove</button>
        </div>
      )}

      <div className="box">
        <img className="randomQuote" src={randomData} alt=""/>
        <button onClick={() => setRandomData(getRandomObject(DATA))}>รับกำลังใจ</button>
      </div>
    </div>
  );
}


export default BoxofEn;
