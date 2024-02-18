import React, { useState, useEffect } from 'react';
import KatexSpan from './KatexSpan';
import ImagePaster from './ImagePaster';

function VideoPlayer() {
    const [mp4Url, setMp4Url] = useState('');
    const [explanation, setExplanation] = useState('');
    const [loadingText, setLoadingText] = useState('');

    

  const handlePaste = async (event: any) => {
    const clipboardData = event.clipboardData //|| window.clipboardData;
    if (clipboardData) {
      const items = clipboardData.items;
      for (let index in items) {
        const item = items[index];
        if (item.kind === 'file') {
          const blob = item.getAsFile();
          const reader = new FileReader();
          reader.onload = function(event) {
            let  base64data;
            if(event.target)
            {
                base64data = event.target.result;
                if(base64data)
                {
                    sendToBackend(base64data);
                }
                
            }
            
          };
          reader.readAsDataURL(blob);
        }
      }
    }
  };

  const sendToBackend = async (data: any) => {
    // Use fetch or Axios to send data to the backend
    setLoadingText('Loading...');
    try {
      const response = await fetch('http://localhost:5000/generate_video_base64', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ screenshotData: data }),
      });
      let blob = await response.blob();
    //console.log(response)
    
    const videoUrl = URL.createObjectURL(blob);
    // console.log(`URL${videoUrl}`)
    // console.log(typeof(videoUrl))
    // Set the URL of the received MP4 file
    setMp4Url(videoUrl);

    // get new explanation for video
    let response2 = await fetch('http://localhost:5000/get_explanation');
    let explanation = await response2.json();
    console.log(explanation)
    setExplanation(explanation.explanation);
    setLoadingText('');
    } catch (error) {
      console.error('Error sending data to backend:', error);
    }
  };


    
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
        setLoadingText('');

        
        }
        catch(error)  {
            console.error('Error fetching MP4 file:', error);
        };
    };
  

    return (
        <div className="flex flex-col bg-biddle-white gap-4 min-h-[800px] items-center pb-20 p-4 rounded-3xl w-2/3 border-4 border-black">
            <div className="flex flex-col gap-4">
                <h2 className="font-bold w-64 text-center text-xl">Take a screenshot and paste it here</h2>
                <div
                    contentEditable={true} // Allows the div to accept pasted content
                    onPaste={handlePaste} // Handle the paste event
                    className="border-4 border-black p-4 min-h-24 rounded-lg flex justify-center items-center bg-white"
                    // style={{ border: '1px solid black', padding: '20px' }}
                >
                
                </div>
            </div>
            <div className="flex flex-col gap-4 items-center">
                {/* <button onClick={sendRequestToFlask} className="px-8 py-4 bg-white border-2 border-black rounded-lg transition-color hover:bg-black hover:text-white active:translate-y-2">
                Test
                </button> */}
                <p>{loadingText}</p>
                {mp4Url === '' ? <p></p> : <div className="flex flex-col items-center">
                <video className="border-8 border-gray-400 rounded shadow-[0px_4px_16px_rgba(17,17,26,0.1),_0px_8px_24px_rgba(17,17,26,0.1),_0px_16px_56px_rgba(17,17,26,0.1)]" key={mp4Url} width="640" height="480" controls>
                    <source src={mp4Url} type="video/mp4" />
                    Your browser does not support the video tag.
                </video>
                <div className="w-64 my-8 h-0 border-2 border-black"/>
                  </div>}
                {/* <video key={mp4Url} width="640" height="480" controls>
                    <source src={mp4Url} type="video/mp4" />
                    Your browser does not support the video tag.
                </video> */}
                {/* <button onClick={ () => console.log(mp4Url)} className="px-8 py-4 bg-white border-2 border-black rounded-lg transition-color hover:bg-black hover:text-white active:translate-y-2">
                log
                </button> */}
            </div>
            <KatexSpan text={explanation}></KatexSpan>
        </div>
    );
}

export default VideoPlayer;
