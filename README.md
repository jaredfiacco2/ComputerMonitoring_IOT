<!-- PROJECT SHIELDS -->
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/jaredfiacco2/FirebasePodcastTranscription">
    <img src="images/transcript.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Monitor Computer's Stats, Store in Google Cloud</h3>

  <p align="center">
    This code uses python to publish computer statistics to BigQuery using Pub/Sub and Cloud Functions.
    <br />
    <br />
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#prerequisites">Prerequisites & Instructions</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

- Wouldn't it be great to see how your computers' CPU usage and other stats change over time, stornig it for future analysis?

- In this project, I use python to publish data to Google Pub/Sub, and use Google Functions on-demand computing to take published data and store it in BigQuery for future use.

<img src="images\ProcessMap.png" alt="Process Map"/>

### Built With

* [Python](https://python.org)
* [Pub/Sub](https://cloud.google.com/pubsub)
* [Cloud Functions](https://cloud.google.com/functions)
* [BigQuery](https://cloud.google.com/bigquery)

### Prerequisites & Instructions

1. Installing all Required Packages
  ```sh
  pip install -r requirements.txt
  ```

2. Open a Google Cloud Platform Account and create a new project. 

3. Open the IAM & Admin page, set up permissions and obtain an API key.
<img src="images\Step1_IAM_Admin.png" alt="set up permissions" />

4. Set up the Cloud Function to pull the Pub/Sub data when it's published and append it to BigQuery.
<img src="images\Step2_CloudFunctions.png" alt="set up cloud fucntions" />

5. Use Pub/Sub Metrics and Logs to troubleshoot any issues you have.
<img src="images\CloudFunctions_Metrics.png" alt="check pub/sub metrics and logs" />

6. Use BigQuery to check query your computers' stats over time.
<img src="images\Step4_BigQuery.png" alt="use BigQuery to query the stats" />

<!-- CONTACT -->
## Contact

[Jared Fiacco](https://www.linkedin.com/in/jaredfiacco/) - jaredfiacco2@gmail.com

My Similar Project: [Transcribe Podcasts, Save to GCP Firebase](https://github.com/jaredfiacco2/FirebasePodcastTranscription)



This project was inspired by:
[IOT Weather Station using Pub/Sub](https://medium.com/@serbelga/build-a-weather-station-with-google-cloud-iot-cloud-firestore-mongoose-os-android-jetpack-350556d7a)
[PubSub to BigTable Using Cloud Functions](https://itnext.io/pubsub-to-bigtable-piping-your-data-stream-in-via-gcp-cloud-functions-a2ef785935b5)



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/jaredfiacco/