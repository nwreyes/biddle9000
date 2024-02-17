"use client";
// Import statements if necessary

// Define a function to send a request to the Flask backend
const sendRequestToFlask = async () => {
  try {
    // Make a GET request to the Flask backend
    const response = await fetch('http://localhost:5000/');
    
    // Check if the response is successful (status code 200)
    if (response.ok) {
      // If successful, parse the response text
      const data = await response.text();
      
      // Log the response from Flask
      console.log(data);
    } else {
      // If the response is not successful, throw an error
      throw new Error('Failed to fetch data from Flask server');
    }
  } catch (error) {
    // Log any errors that occur during the fetch request
    console.error('Error fetching data:', error);
  }
};



export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <div className="z-10 max-w-5xl w-full items-center justify-between font-mono text-sm lg:flex">
        <p className="fixed left-0 top-0 flex w-full justify-center border-b border-gray-300 bg-gradient-to-b from-zinc-200 pb-6 pt-8 backdrop-blur-2xl dark:border-neutral-800 dark:bg-zinc-800/30 dark:from-inherit lg:static lg:w-auto  lg:rounded-xl lg:border lg:bg-gray-200 lg:p-4 lg:dark:bg-zinc-800/30">
          Get started by editing&nbsp;
          <code className="font-mono font-bold">app/page.tsx</code>
        </p>
        <button onClick={sendRequestToFlask} className="flex w-full justify-center border-b border-gray-300 bg-gradient-to-b from-zinc-200 pb-6 pt-8 backdrop-blur-2xl dark:border-neutral-800 dark:bg-zinc-800/30 dark:from-inherit lg:static lg:w-auto  lg:rounded-xl lg:border lg:bg-gray-200 lg:p-4 lg:dark:bg-zinc-800/30">
          Test
          on
        </button>
      </div>
    </main>
  );
}
