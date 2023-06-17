# Apache_App_Proje

This repository contains the code and resources for the Apache_App_Proje project.

## Description
Apache_App_Proje is a Python application that demonstrates a real-time messaging system. It utilizes Apache as a web server, MongoDB as the database, and implements a producer-consumer architecture to send and receive messages based on changes in the connected MongoDB database. The project aims to provide an example of how to create a reactive system using Apache, MongoDB, and Python.

## Build and Run Steps

To build and run the Apache_App_Proje application, follow the steps below:

1. **Clone the repository:**
git clone https://github.com/TheCrks/Apache_App_Proje.git

2. **Install Python and Dependencies:**
- Install Python on your system by visiting the official Python website (https://www.python.org/downloads) and downloading the appropriate version for your operating system.
- Open a terminal or command prompt and navigate to the cloned repository.
- Install the required dependencies by running the following command:
  ```
  pip install -r requirements.txt
  ```

3. **Set Up Apache and MongoDB:**
- Install Apache and MongoDB on your system by following their respective installation instructions. Ensure they are both running properly.

4. **Configure Apache:**
- Copy the project files from the cloned repository to the appropriate directory in the Apache document root, typically `/var/www/html/` on Linux or `C:\Apache\htdocs\` on Windows.
- Configure any necessary virtual hosts or server settings based on your specific requirements.

5. **Run the Producer and Consumer:**
- Open a terminal or command prompt.
- Navigate to the `producer` directory within the cloned repository.
- Start the producer application by running the following command:
  ```
  python producer.py
  ```
- Open another terminal or command prompt.
- Navigate to the `consumer` directory within the cloned repository.
- Start the consumer application by running the following command:
  ```
  python consumer.py
  ```

6. **Test the Application:**
- Make changes to the connected MongoDB database (e.g., create, update, or delete documents).
- The producer application will detect the changes and send messages to the consumer.
- The consumer application will receive and print out the messages in the terminal or command prompt.

## Additional Information
- Ensure that you have the necessary permissions and dependencies installed for running Apache, MongoDB, and the Python application.
- Customize the MongoDB connection settings in the producer and consumer scripts if your MongoDB instance is running on a different host or port.
- Feel free to modify the README.md file as needed to provide additional information or clarify any specific instructions related to your project.
