# Internet-Speed-Twitter-Complaint-Bot

A Python bot that automatically performs an internet speed test, scrapes the results, logs into your Twitter account, and tweets a complaint about your internet speed (if it's slow).

## Features

- **Automated Speed Testing**: Uses Selenium to start a speed test and capture the results.
- **Real-Time Speed Data**: Scrapes the download and upload speeds once the test is completed.
- **Automated Twitter Interaction**: Logs into your Twitter account and posts a complaint tweet if the speed is below a specified threshold.

## Getting Started

### Prerequisites

- Python 3.x
- Required libraries:
- `selenium`
- ChromeDriver (for Selenium to interact with the browser)

### Installing Dependencies

1. Install Python dependencies:


   ```bash
   pip install selenium
   ```
## How to Use

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yingliu1206/Internet-Speed-Twitter-Complaint-Bot.git
   cd Internet-Speed-Twitter-Complaint-Bot
   ```
   
2. **Add your Twitter credentials:**:
   ```bash
   twitter_username = 'your_username'
   twitter_password = 'your_password'
   ```

4. **Set your speed threshold (optional):**:
  - You can set a threshold for the download speed (in Mbps). If the speed is below this threshold, the bot will tweet a complaint.

   ```bash
   SPEED_THRESHOLD = 300  # Adjust as needed (e.g., 300 Mbps)
   ```
     
6. **Run the program**:
  - Run the script, which will start the speed test, capture the results, and tweet a complaint if the speed is below the set threshold:

   ```bash
   python main.py
   ```

## Example Tweet
  - If the download speed is below your set threshold, the bot will automatically tweet something like:

```bash
  Hey [Network Provider], why is my internet so slow? 😡
  📶 Download Speed: 25 Mbps
  📤 Upload Speed: 10 Mbps
```
   
## Acknowledgments
- [100 Days of Code: The Complete Python Pro Bootcamp - Udemy](https://www.udemy.com/course/100-days-of-code) for the inspiration and guidance.
