from openai import OpenAI
import os 
import config
os.environ["OPENAI_API_KEY"] = config.OPENAI_KEY


client = OpenAI()

def parseImage():

    client = OpenAI()

    response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
        {
        "role": "user",
        "content": [
            {"type": "text", "text": "The following is a screenshot of a math equation or matrix or similar math object. Please write the equation as a string. If it is a matrix or vector, format it as [[a, b], [c, d]]"},
            {
            "type": "image_url",
            "image_url": {
                "url": "https://i.redd.it/a65fiaqmyh681.jpg",#https://miro.medium.com/v2/resize:fit:640/format:webp/1*-PGZIOCgY_qbzeI_yGFO4A.png
            },
            },
        ],
        }
    ],
    )

    print("RESPONSE:"+response.choices[0].message.content)

    response = client.chat.completions.create(
    model="gpt-4-1106-preview",
    messages=[
        {
        "role": "user",
        "content": [
            {"type": "text", "text": f" Output this as latex. {response.choices[0].message.content}\n\n ONLY the equation in latex such as \int (u dv). DO NOT output anything other than the latex."}
        ],
        }
    ],
    )
    print(response.choices[0].message.content)
    value = response.choices[0].message.content.replace('{{', '{ {').replace('}}', '} }')


    return value