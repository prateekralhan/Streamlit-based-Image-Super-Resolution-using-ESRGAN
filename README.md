# Streamlit based ISR using ESRGAN [![Project Status: Active](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active) [![](https://img.shields.io/badge/Prateek-Ralhan-brightgreen.svg?colorB=ff0000)](https://prateekralhan.github.io/)
A simple streamlit based webapp demonstrating Image Super Resolution using [ESRGAN.](https://github.com/xinntao/ESRGAN)

## Installation:
* Simply run the command ***pip install -r requirements.txt*** to install the dependencies.

## Usage:
1. Clone this repository and install the dependencies as mentioned above.
2. Make a directory within this cloned repository with the name `.streamlit` *(Don't forget the dot !!)*.
3. Create a file `config.toml` in this directory *(Be aware of the file extension !!)*.
4. Copy-Paste the following contents in this file and save :
```
[theme]
primaryColor="#b11b1b"
backgroundColor="#080e1c"
secondaryBackgroundColor="#203659"
textColor="#bf7c7c"
```
5. Navigate to the root directory and create another directory with the name `models`.
6. Download pretrained models from [here](https://drive.google.com/drive/u/0/folders/17VYV_SoZZesU6mbxz2dMAIccSSlqLecY), and place them inside this directory.
7. Navigate to the root directory of this repository and simply run the command: 
```
streamlit run app.py
```
Navigate to http://localhost:8501 in your web-browser.

![1](https://user-images.githubusercontent.com/29462447/159141437-1d667923-2af6-40e4-a50b-3a6cc7075471.png)

![2](https://user-images.githubusercontent.com/29462447/159141435-ef7477f3-f9a3-48da-a29d-51a3c85f3ee8.png)

8. By default, streamlit allows us to upload files of **max. 200MB**. If you want to have more size for uploading files, execute the command :
```
streamlit run app.py --server.maxUploadSize=1028
```


### Running the Dockerized App
1. Ensure you have Docker Installed and Setup in your OS (Windows/Mac/Linux). For detailed Instructions, please refer [this.](https://docs.docker.com/engine/install/)
2. Navigate to the folder where you have cloned this repository ( where the ***Dockerfile*** is present ).
3. Build the Docker Image (don't forget the dot!! :smile: ): 
```
docker build -f Dockerfile -t app:latest .
```
4. Run the docker:
```
docker run -p 8501:8501 app:latest
```

This will launch the dockerized app. Navigate to ***http://localhost:8501/*** in your browser to have a look at your application. You can check the status of your all available running dockers by:
```
docker ps
```
