# Whatsapp Analyzer
This analysis is built as a gift for my girlfriend. I'll be analyzing the whatsapp chat history over the history of our relationship, as well as scraping call data to analyze our phonecall history.

The chat data can easily be exported by whatsapp to a CSV file, but the call data has been harder to analyze.
After much research, and contacting whatsapp to find out they don't allow access to this data, I decided to scrape the data myself.
This was accomplished through utilizing Samsung DeX and a script to screenshot every call log in my call history.
After collecting a screenshot of every call through this script, I processed the images using cv2 and ran pytesseract OCR on the images to scrape the text.
This outputted text ended up being a jumbled mess, but had somewhat of a pattern, so I used regex to clean up what I could programatically, then exported it to excel to finish the cleanup manually.

Once all the data was cleaned, primarily pandas and seaborn were used to analyze it. All analysis were collected and exported to an external word document manually to present to my girlfriend(Who loved seeing how many emojis we sent and our total call time haha!)

