import React, { useState, useEffect } from 'react';

function VideoPlayer() {
    const [mp4Url, setMp4Url] = useState('');
    
    // Define a function to send a request to the Flask backend
    const sendRequestToFlask = async () => {
        try {
        // Make a GET request to the Flask backend
        let response = await fetch('http://localhost:5000/generate_video');
        let blob = await response.blob();
        console.log(response)
        
        const videoUrl = URL.createObjectURL(blob);
        console.log(`URL${videoUrl}`)
        console.log(typeof(videoUrl))
        // Set the URL of the received MP4 file
        setMp4Url(videoUrl);
        
        }
        catch(error)  {
            console.error('Error fetching MP4 file:', error);
        };
    };
  

    return (
        <div className="border-2 border-white">
            <button onClick={sendRequestToFlask} className="flex w-full justify-center border-b border-gray-300 bg-gradient-to-b from-zinc-200 pb-6 pt-8 backdrop-blur-2xl dark:border-neutral-800 dark:bg-zinc-800/30 dark:from-inherit lg:static lg:w-auto  lg:rounded-xl lg:border lg:bg-gray-200 lg:p-4 lg:dark:bg-zinc-800/30">
            Test on
            </button>
            <video key={mp4Url} width="640" height="480" controls>
                <source src={mp4Url} type="video/mp4" />
                Your browser does not support the video tag.
            </video>
            <button onClick={ () => console.log(mp4Url)} className="flex w-full justify-center border-b border-gray-300 bg-gradient-to-b from-zinc-200 pb-6 pt-8 backdrop-blur-2xl dark:border-neutral-800 dark:bg-zinc-800/30 dark:from-inherit lg:static lg:w-auto  lg:rounded-xl lg:border lg:bg-gray-200 lg:p-4 lg:dark:bg-zinc-800/30">
            log
            </button>
        </div>
    );
}

export default VideoPlayer;
