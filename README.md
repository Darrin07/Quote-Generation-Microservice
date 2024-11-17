# Quote-Generation-Microservice

README Instructions

Communication Contract
To request data from the microservice:
•	Make a GET request to the endpoint /api/quote.
•	Required parameters: user_id (integer) and progress_level (string).
•	Example call:
import requests
response = requests.get("http://localhost:5000/api/quote", params={"user_id": 123, "progress_level": "50%"})
               
               print(response.json())

To receive data from the microservice:
•	The microservice will respond with a JSON object containing the requested quote.
•	Example response:
{
  "user_id": 123,
  "quote": "You're halfway there! Keep up the great work!"
               }

UML Sequence Diagram
![Project Screenshot](assets/image1.jpg)

