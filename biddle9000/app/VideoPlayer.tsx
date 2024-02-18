import React, { useState, useEffect } from 'react';
import KatexSpan from './KatexSpan';

function VideoPlayer() {
    const [mp4Url, setMp4Url] = useState('');
    const [explanation, setExplanation] = useState('');
    const [loadingText, setLoadingText] = useState('');
    
    // Define a function to send a request to the Flask backend
    const sendRequestToFlask = async () => {
        try {
        // Make a GET request to the Flask backend
        setLoadingText('Loading...');
        let response = await fetch('http://localhost:5000/generate_video');
        let blob = await response.blob();
        console.log(response)
        
        const videoUrl = URL.createObjectURL(blob);
        console.log(`URL${videoUrl}`)
        console.log(typeof(videoUrl))
        // Set the URL of the received MP4 file
        setMp4Url(videoUrl);

        // get new explanation for video
        let response2 = await fetch('http://localhost:5000/get_explanation');
        let explanation = await response2.json();
        console.log(explanation)
        setExplanation(explanation.explanation);

        
        }
        catch(error)  {
            console.error('Error fetching MP4 file:', error);
        };
    };
  

    return (
        <div className="flex flex-col gap-4 items-center p-4 rounded-3xl">
            <div className="flex gap-4 items-center">
                <button onClick={sendRequestToFlask} className="px-8 py-4 bg-white border-2 border-black rounded-lg transition-color hover:bg-black hover:text-white active:translate-y-2">
                Test
                </button>
                {mp4Url === '' ? <p>{loadingText}</p> : <video key={mp4Url} width="640" height="480" controls>
                    <source src={mp4Url} type="video/mp4" />
                    Your browser does not support the video tag.
                </video>}
                {/* <video key={mp4Url} width="640" height="480" controls>
                    <source src={mp4Url} type="video/mp4" />
                    Your browser does not support the video tag.
                </video> */}
                <button onClick={ () => console.log(mp4Url)} className="px-8 py-4 bg-white border-2 border-black rounded-lg transition-color hover:bg-black hover:text-white active:translate-y-2">
                log
                </button>
            </div>
            <KatexSpan text={explanation}></KatexSpan>
        </div>
    );
}

export default VideoPlayer;
