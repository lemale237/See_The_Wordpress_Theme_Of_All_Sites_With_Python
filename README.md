# See_The_Wordpress_Theme_Of_All_Sites_With_Python


**Wordpress Theme Detector**

This Python script detects the Wordpress theme used on a website by searching for links to external CSS stylesheet files.

**Usage**

    Install the required dependencies:

pip install requests beautifulsoup4

Run the script by entering the website's URL:

python wordpress_theme_detector.py

You can also specify the URL directly using the -u or --url option:

python wordpress_theme_detector.py --url https://www.example.com

The script will display the link to the theme's CSS file if one is found.
