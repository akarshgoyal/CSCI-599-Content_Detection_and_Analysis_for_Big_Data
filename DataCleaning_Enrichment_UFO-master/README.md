
**Script/Code for Part1-OCR using Tesseract**:

1. Ocr_bash_original.sh - slightly modified OCR pipeline initially provided to us with the same semantics.
2. Clean_out.py - script to traverse through the different folders(outtxt containing all the .txt files) and collect text for cleaning and extraction of required fields into different rows of V2.


**Script/Code for Part2-CV using TikaAndVision and ImageCaption**:

1. scrape_urls.py - It basically scrapes some urls and when access is blocked (after ~200 hits), restarts the web driver and the vpn. Vpn had to be enabled manually but somehow figured out a way to start it with selenium.


2. filter_urls.py - It discards unsupported files using file-extension (metadata)


3. make_urls_https.py - This script converts URLs to well-formed URLs of the form https://example.com/URI


4. download_images.py - It downloads the images at the provided well formed URLs.


5. download_videos.py - It downloads the videos at the provided well formed URLs.


6. separate_images_videos.py - Based on the url postfix, divide the urls into image_urls or video_urls for separate scraping.


7. json_to_csv.py - This script basically converts the objects.json and captions.json to csv files.


8. Bash_cmds.txt - This was used to make Rest calls to docker tensorflow server for object recognition and image captioning.


**Script files for CoreNLP, OpenNLP, MITIE, NLTK**:

CoreNLP, OpenNLP, MITIE, and NLTK libraries were implemented for NER on Textual Description of the newly appended part of V2 dataset. 
