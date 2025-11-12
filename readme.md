# Aquascape Haven

Welcome to your home of all things aquascape, whether you're a beginner or a seasoned veteran this is your space to get inspiration, tips and help with your fish, plants and more!

## User requirements:

+ A gallery on the home page to show off all the beautiful aquascapes that are possible with a little inspiration.
+ Links in the top navbar to all other pages described below. Links in the footer to social media pages.
+ A tracker to allow customers to be able to see the development of their tanks, fish, plants and water parameters.
+ A marketplace for shopping all things aquascape, including but not limited to, tanks, plants, meds, tools, CO2 systems etc. (This will utilise Stripe payments)
+ A community hub for clients to post their wins, get advice and just generally chat all things aquascape. (This will utilise Django)
+ Aquascape of the month will be a competion page for clients to pick their favorites with comments, likes and possibly prizes.

## Testing

### Automated testing:

+ The first Django app I created was `gallery`, this is the simplest of all of my apps. The test I ran was simply to check both the model and the view to ensure the information being inputted was being read and fed back correctly. All of the tests for this came back perfectly. They can be found at: ![gallery] (C:\Users\14sam\.vscode\aquascape-haven\gallery\tests.py)
+ The next app I tested was my `community` app which needed to be tested for both user authentication and post requirements. I created three failing tests in my `community/tests/test_view.py` to test all of the above. The first issue i encountered was that i had linked the whole app up incorrectly. The initial correction to solve this was to back track a little and see if i could get the app working generally on the local server.