import React, { useState, useEffect } from "react";
import './Background.css';
import BoxOf from "./BoxOf";
import icon_up1 from './image/icon_up1.png';
import Spotify from "./Spotify";

function BackgroundHome() {
    const [bg_img, setImage] = useState('https://64.media.tumblr.com/27939018ad44f1840a7af7e9d07746a6/tumblr_pmw2z728IN1uvsi7jo3_1280.gifv')
    const changeBg1 = () => {setImage('https://i.pinimg.com/originals/ef/21/20/ef212097b6111cd26f33b5373dbaf544.gif');};
    const changeBg2 = () => {setImage('https://i.pinimg.com/originals/4e/80/38/4e8038228e029c3ddd9c7b90b293af9d.gif');};
    const changeBg3 = () => {setImage('https://i.pinimg.com/originals/85/bf/2c/85bf2cd735d075bb9ece4be5996605b1.gif');};
    const changeBg4 = () => {setImage('https://i.pinimg.com/originals/52/86/71/528671b25753cd9e4f5e48c1586ae88b.gif');};
    const changeBg5 = () => {setImage('https://i.pinimg.com/originals/52/86/71/528671b25753cd9e4f5e48c1586ae88b.gif');};
    function uploadFile(e) {
        console.log(e.target.files);
        setImage(URL.createObjectURL(e.target.files[0]));
    }
        return (
            <div className="contain">
                <header>
                    <h1>Let Me Sea</h1>
                </header>
                <img className="bg1" src={bg_img} alt=""></img>
                <div className="contain_btn">
                    <button className="btn1" type="button" onClick={changeBg1}><img alt="" className="img_btn"src="https://i.pinimg.com/originals/ef/21/20/ef212097b6111cd26f33b5373dbaf544.gif"/></button>
                    <button className="btn2" type="button" onClick={changeBg2}><img alt="" className="img_btn"src="https://i.pinimg.com/originals/4e/80/38/4e8038228e029c3ddd9c7b90b293af9d.gif"/></button>
                    <button className="btn3" type="button" onClick={changeBg3}><img alt="" className="img_btn"src="https://i.pinimg.com/originals/85/bf/2c/85bf2cd735d075bb9ece4be5996605b1.gif"/></button>
                    <button className="btn4" type="button" onClick={changeBg4}><img alt="" className="img_btn"src="https://i.pinimg.com/originals/52/86/71/528671b25753cd9e4f5e48c1586ae88b.gif"/></button>
                    <button className="btn5" type="button" onClick={changeBg5}><img alt="" className="img_btn"src="https://i.pinimg.com/originals/52/86/71/528671b25753cd9e4f5e48c1586ae88b.gif"/></button>
                </div>
                <input type="file" 
                    accept="image/*" 
                    id="fileBg"
                    onChange={uploadFile}/>
                <label htmlFor="fileBg"><img src={icon_up1} alt="" className="upload_icon"></img></label>
                <BoxOf/>
            </div>
        );

}


export default BackgroundHome;
