# Smart Solutions For Railways

### Project Description:

Smart Solutions for railways is designed to reduced the work load of the user and also the use of paper.

#### Features:

- A Web page is designed for the public where they can book tickets by seeing the available seats.
- After booking the train, the person will get a QR code which has to be shown to the Ticket Collector while boarding the train.
- The ticket collectors can scan the QR code to identify the personal details.
- A GPS module is present in the train to track it. The live status of the journey is updated in the Web app continuously
- All the booking details of the customers will be stored in the database with a unique ID and they can be retrieved back when the Ticket Collector scans the QR Code.

### Project Objectives

The objective of this project is to

- Develop a web app for booking the tickets.
- Gain knowledge of Watson IoT Platform.
- Connecting IoT devices to the Watson IoT platform and exchanging the sensor data.
- Gain knowledge on IBM Cloudant DB
- Explore Python client libraries of Watson IoT Platform.
- Explore Python library for integrating OpenCV for accessing the Live Camera Input
- Scan the QR code in live streaming and retrieve the QR code details
- Gain knowledge on web application development.
- Gain knowledge of storing the data in Cloudant DB
- Generating QR codes with the required data

#### Project Flow:

- Using the Web application, a user books a ticket based on the availability of the seats by giving the general required information.
- Once a user clicks on the submit button, a QR code is generated with a Unique ID and the data is stored in the Cloudant DB with that Unique ID.
- Users can save the QR code for further process.
- In python code, a Ticket collector can scan the QR code and extract the information from the QR Code i.e., Unique ID. With that Unique ID, data is fetched from the Cloudant DB, if it is not found, then it displays Not a Valid Ticket.
- Also, the live location of the train will be published to IBM IoT platform using python code
- The train location can be tracked from a Web Application.
