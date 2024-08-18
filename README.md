# WebShield

Welcome to WebShield, a comprehensive solution designed to enhance online safety by identifying and alerting users to potential phishing threats. WebShield is a Chrome extension combined with a ReactJS-based web application that leverages machine learning models to detect phishing sites. The project integrates a Firebase cloud database to manage and track phishing submissions, providing an interactive platform similar to PhishTank.

## Overview of WebShield

WebShield offers a robust and user-friendly approach to phishing detection and alerting, ensuring safer browsing experiences for users. Here's what WebShield delivers:

### Chrome Extension Features:
- **Real-Time Phishing Alerts**: As you browse, the extension monitors URLs and alerts you if a website is suspected of phishing, powered by a machine learning model.
- **User Interface**: The extension provides an intuitive interface with a small pop-up displaying an alert message if the site is potentially harmful, including options to visit the site regardless.

### Web Application Features:
- **Phish Search**: Browse a list of phishing submissions, including ID, URL, and verification status (displayed in red for "Not verified" and green for "Verified").
- **Submit Suspected Phishes**: Users can easily submit URLs they believe to be phishing attempts. A simple input box and submission button make it quick and efficient.
- **Track Submission Status**: Users can track the status of their submissions, whether they have been verified or are still under review.
- **Verify Other Submissions**: Help the community by verifying URLs submitted by others, improving the overall accuracy and reliability of the database.
- **Recent Submissions**: A section dedicated to displaying the most recent phishing URLs submitted by users, including ID, URL, and date of submission, with an option to verify.

### Machine Learning Integration:
- **Phishing Detection Model**: WebShield uses a trained machine learning model to analyze URLs and detect potential phishing sites. The model is continuously improved with new data from user submissions.

### Firebase Integration:
- **Cloud Database**: Firebase is utilized to store phishing URLs, user submissions, and verification statuses, ensuring that data is securely stored and easily accessible.
- **Real-Time Updates**: The use of Firebase allows for real-time updates to the web application, ensuring that users always have the most current data.

### UI and Design:
- **ReactJS and Bootstrap**: The web application is built using ReactJS, and Bootstrap is integrated to ensure a responsive and modern user interface. This combination provides a clean, intuitive design, making the application easy to navigate.

## Structure of the Repository

- **Running the Project**:
  - [`main_script.sh`](https://github.com/fromjyce/WebShield/blob/main/main_script.sh) - Main script to run the project.

- **Chrome Extension**: 
  - [`popup.html`](https://github.com/fromjyce/WebShield/blob/main/extension/popup.html) - The HTML structure of the extension's popup interface.
  - [`popup.js`](https://github.com/fromjyce/WebShield/blob/main/extension/popup.js) - JavaScript logic for handling user interactions within the popup.
  - [`manifest.json`](https://github.com/fromjyce/WebShield/blob/main/extension/manifest.json) - Configuration file for the Chrome extension.

- **Web Application**:
  - [`src/`](https://github.com/fromjyce/WebShield/tree/main/webshield-website/src) - Contains all React components, including the main interface and individual features such as the Phish Search, Submission form, and Recent Submissions.
  - [`firebase.js`](https://github.com/fromjyce/WebShield/blob/main/webshield-website/src/firebase.js) - Firebase configuration and initialization.
  - [`App.js`](https://github.com/fromjyce/WebShield/blob/main/webshield-website/src/App.js) - Main application logic and routing.
  - [`styles/`](https://github.com/fromjyce/WebShield/tree/main/webshield-website/src/styles) - Custom CSS files for additional styling alongside Bootstrap.

- **Machine Learning Model**:
  - [`model_development/`](https://github.com/fromjyce/WebShield/tree/main/model%20development) - Directory containing the trained machine learning model and related scripts.
  - [`model_training.py`](https://github.com/fromjyce/WebShield/blob/main/model%20development/model_training.py) - Python script used to train the phishing detection model.

## Running the Project

### Chrome Extension:
1. Clone the repository.
2. Load the Chrome extension by navigating to `chrome://extensions/` in your browser and selecting "Load unpacked."
3. Choose the directory containing the `manifest.json` file.

### Web Application:
1. Clone the repository and navigate to the [`webshield-website`](https://github.com/fromjyce/WebShield/tree/main/webshield-website) directory.
2. Install the necessary dependencies using `npm install`.
3. Start the development server using `npm start`.

### Machine Learning Model:
1. Run [`model_training.py`](https://github.com/fromjyce/WebShield/blob/main/model%20development/model_training.py) to train the phishing detection model.
2. Integrate the trained model into the Chrome extension for real-time phishing detection.

## Contact

If you come across any issues, have suggestions for improvement, or want to discuss further enhancements, feel free to contact me at [jaya2004kra@gmail.com](mailto:jaya2004kra@gmail.com). Your feedback is greatly appreciated.

## License

All the code and resources in this repository are licensed under the GNU General Public License. You are free to use, modify, and distribute the code under the terms of this license. However, I do not take responsibility for the accuracy or reliability of the programs.

## My Social Profiles:

- [**LinkedIn**](https://www.linkedin.com/in/jayashrek/)