import React, { useState } from 'react';

function ImagePaster() {


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
    try {
      const response = await fetch('http://localhost:5000/generate_video_base64', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ screenshotData: data }),
      });
      const responseData = await response.json();
      console.log(responseData);
    } catch (error) {
      console.error('Error sending data to backend:', error);
    }
  };

  return (
    <div>
        <h2>Copy a screenshot and paste it here</h2>
        <div
            contentEditable={true} // Allows the div to accept pasted content
            onPaste={handlePaste} // Handle the paste event
            style={{ border: '1px solid black', padding: '20px' }}
        >
        
        </div>
    </div>
  );
}

export default ImagePaster;
