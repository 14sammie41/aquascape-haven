# Aquascape Haven

Welcome to your home of all things aquascape, whether you're a beginner or a seasoned veteran this is your space to get inspiration, tips and help with your fish, plants and more!

## User requirements:

+ A gallery on the home page to show off all the beautiful aquascapes that are possible with a little inspiration.
+ Links in the top navbar to all other pages described below. Links in the footer to social media pages.
+ A tracker to allow customers to be able to see the development of their tanks, fish, plants and water parameters.
+ A marketplace for shopping all things aquascape, including but not limited to, tanks, plants, meds, tools, CO2 systems etc. (This will utilise Stripe payments)
+ A community hub for clients to post their wins, get advice and just generally chat all things aquascape. (This will utilise Django)
+ Aquascape of the month will be a competion page for clients to pick their favorites with comments, likes and possibly prizes.

### Wireframe

This was a very organic build for me so this wireframe is extremely simple. Apologies:
+ ![Wireframe](static/images/wireframe-mockup.png)

## Database Schema

Below is an overview of the main models and their relationships in Aquascape Haven:

![Schema](static\images\aquascape-schema.png)

### User (Django default)
- `id` (PK)
- `username`
- `email`
- `password`
- ...other Django auth fields

### Gallery
- `id` (PK)
- `title`
- `description`
- `image` (ImageField)
- `user` (FK to User)
- `created_at`

### CommunityPost
- `id` (PK)
- `user` (FK to User)
- `title`
- `content`
- `image` (ImageField, optional)
- `created_at`
- `updated_at`

### CommunityComment
- `id` (PK)
- `post` (FK to CommunityPost)
- `user` (FK to User)
- `content`
- `created_at`

### MarketplaceProduct
- `id` (PK)
- `name`
- `description`
- `price`
- `image` (ImageField)
- `stock`
- `category`
- `created_at`

### Order
- `id` (PK)
- `user` (FK to User)
- `order_number`
- `created_at`
- `status`
- `total`
- ...other order fields

### OrderItem
- `id` (PK)
- `order` (FK to Order)
- `product` (FK to MarketplaceProduct)
- `quantity`
- `price`

### Tracker
- `id` (PK)
- `user` (FK to User)
- `tank_name`
- `fish`
- `plants`
- `water_parameters` (JSONField or TextField)
- `created_at`
- `updated_at`

---

**Legend:**  
- PK = Primary Key  
- FK = Foreign Key  
- ManyToManyField = Many-to-many relationship

This schema covers users, gallery, community, marketplace, orders, and tank tracking.

## Tech Stack

- **Backend**: Django, Python
- **Frontend**: Bootstrap 5, Flexbox, custom CSS
- **Database**: PostgreSQL (Heroku)
- **Deployment**: Heroku
- **Storage**: AWS S3 for media files
- **Version Control**: Git & GitHub

### Dependencies and Credits

This will be for dependencies as I go through this project - complete as they come through.
+ [Bootstrap](https://getbootstrap.com/) has been used throughout the project to add items like a navbar, styling and a footer. I have annotated throughout the project, the key areas this has been used.
+ [Microsoft CoPilot](https://copilot.microsoft.com/) was used to create AI images to utilize for the Home page and some content in other areas. Also assisted for quick error diagnosis.
+ [Google Fonts](https://fonts.google.com/) used to import two font styles into the style.css file. Both fonts were attributed to the Root in CSS making the styles uniform across the site.
+ [Font Awesome](https://fontawesome.com/) used to import icons for social links in the footer section. Will most likely be used elsewhere too.
+ [Favicon.io](https://favicon.io/#google_vignette) used to create a simple favicon with the correct colors and fonts as used throughout the site. Then link to each page.
+ [IloveIMG.com](https://www.iloveimg.com/) was used to compress all of my images to optimize page load up.
+ [Grammarly](https://app.grammarly.com/ddocs/2742182934) was used to check and correct all of the grammar on this README file.
+ [AWS](https://aws.amazon.com) was used for cloud storage and hosting services (S3 for media, Heroku integration).
+ [Heroku](https://www.heroku.com/) Is my deployment site.

## Deployment

For tutors and examiners please find the live link below:
[Aquascape Haven](https://aquascape-haven-e3d516166de9.herokuapp.com/)

Running the project locally:
1. Ensure you have a GitHub account [Create one here](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github).
2. Use Google Chrome as the best browser for this deployment.
3. Install VSCode to your computer or open the browser version [here](https://vscode.dev/).
4. Click the 'Open Remote Repository' button on the home page to clone and or edit as you wish.

To do the above you may need to follow these steps also:
1. Open the repository in GitHub [here](https://github.com/14sammie41/samantha-spencer)
2. Under the name, click 'clone or download'.
3. Once in the clone section copy the HTTP clone URL for the repository.
4. In the local IDE of your choice, open the terminal.
5. Change the current working directory to wherever you want it to be made.
6. Type `git clone`, and then paste the URL you copied in step 3.

Deployment, step-by-step guide:
+ In GitHub, first, ensure all work is committed and pushed, then go to the settings tab on GitHub, then the Pages section on the left-hand navigation.
+ Once in the Pages section on GitHub change the branch drop down to 'Main' and then click the save option.
+ Now go back to the code section of GitHub and click the deployment link on the right-hand side. (You may need to refresh the page to see the deployment link)
+ Once on the deployment page on GitHub click on the provided link and it will open up the deployed project.

### Setup Instructions

1. Clone the repository:
    git clone https://github.com/yourusername/aquascape-haven.git
    cd aquascape-haven
2. Create and activate a virtual environment:
    python -m venv venv
    source venv/bin/activate   # Mac/Linux
    venv\Scripts\activate      # Windows
3. Install dependancies:
    pip install -r requirements.txt
4. Apply migrations:
    python manage.py migrate
5. Create a superuser:
    python manage.py createsuperuser
6. Run the development server:
    python manage.py runserver

### For Heroku and live deployment:

Ensure you have the follwing pre requisites to start:
+ Heroku CLI installed, follow the link > [Heroku](https://devcenter.heroku.com/articles/heroku-cli)
+ A Git repository for the Django project.
+ A Heroku account (This can be created from the above link)
1. Create required files as below:
    + `pip freeze > requirements.txt`
    + `Procfile`
2. Inside `Procfile` add `web: gunicorn aquascape_haven.wsgi:application`
3. Ensure the `settings.py` file includes all requirements according to respective documentation.
4. Create the Heroku app either in the terminal or on the Heroku website, terminal commands below:
    + `heroku login`
    + `heroku create your-app-name`
5. Set your environment variables as deomnstrated in .env.example .
6. Ensure you run the below commands in the terminal:
    + `python manage.py makemigrations`
    + `python manage.py migrate`
    + `python manage.py collectstatic`
7. The collect static command above is the link to the collect static function in the screenshot below in config vars.
8. Set DEBUG to False for deployment.
9. Add your chosen database and PostgreSQL.
10. Commit your project to GitHub.
11. Link your GitHub in the Heroku Deploy tab.
12. In the Heroku deploy tab, click the Deploy button and wait for it to run.
13. Open App.
+ ![Screenshot of config vars on Heroku](static/images/config-vars.png)
+ ![Screenshot of live homepage]()
+ ![Screenshot of .env.example file](static/images/envfileexample.png)

### Troubleshooting Heroku deployment:

+ If your static files are not loading ensure you have the example config vars set up for `DISABLE_COLLECTSTATIC` and that you have run `python manage.py collectstatic` in your terminal before commiting and deploying your project.
+ If youre database is not connecting make sure you have run your migrations by using `python manage.py migrate` in your terminal before commiting and deploying your project.
+ If the Cloudinary images are not working make sure your config vars are set correctly and check your Cloudinary dashboard for usage issues.
+ If your app won't start you can run `heroku logs --tail` in the terminal to view error messages in the log or loook on the log on the Heroku dashboard.

## Testing

As I have been testing most aspects as I write the code for the site, I am hoping this is not going to be too much.

### Automated testing:

+ The first Django app I created was `gallery`, this is the simplest of all of my apps. The test I ran was simply to check both the model and the view to ensure the information being inputted was being read and fed back correctly. All of the tests for this came back perfectly. They can be found at: ![gallery] (gallery/tests.py)
+ The next app I tested was my `community` app which needed to be tested for both user authentication and posting requirements. I created three failing tests in my `community/tests/test_view.py` to test all of the above. The first issue i encountered was that i had linked the whole app up incorrectly. The initial correction to solve this was to back track a little and see if i could get the app working generally on the local server. Then the rest of the tests can be found at: ![Community](community/tests/test_view.py)

### Testing as a user for navigation purposes:
+ All pages have been checked, all links have been confirmed to work including external links to ensure they open in a new page.
+ I made sure all buttons only show when the right circumstances are met (e.g. ensuring you can't delete a comment if not logged in).
+ I confirmed the page is readable on all screen sizes thanks to Chrome Dev Tools and Bootstrap coding.

### Testing with validators:
+ First validator used was [W3Schools HMTL validator](https://validator.w3.org/#validate_by_input). Expecting possibly some missed slashes, but that should be all.
    + Initial test for home page showed 11 errors, 4 errors regarding backslashes, 3 warnings for first occurunces and some others annotated below:
        + First issue regarding backslashes fixed by swapping to the right slash.
        + All errors regarding ID were fixed by simply removing them as they were not actually in use.
        + Finally I have a warning regarding a section with no header. This is by design as it creates cleaner code so i have left it.
    + Initial test for community page showed only the warning from the section with no header, which as above will be left.
    + Initial test for competition page showed only the warning from the section with no header, which as above will be left.
    + Initial test for gallery page showed only the warning from the section with no header, which as above will be left.
    + Initial test for marketplace page showed only the warning from the section with no header, which as above will be left.
+ Second validator used was [W3Schools CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input). Expecting some syntax errors as I haven't dived as deep on my CSS as I did on my HTML.
    + Two errors found and 21 warnings as described below:
        + First error was regarding a `size` i had put on my social links which is not a CSS property. Changed it to `font-size` as an actual property.
        + Second error was because I had used `center` for a position value. This does not work in CSS. Swapped position out for display and margin to have the same affect with the Bootstrap utilities.
        + I had one warning because an imported file is in the CSS which can safely be ignored.
        + I had 20 warnings because I am using custom styles with the `--var` tag. Again these can be safely ignored.
+ Checked page using Chrome DevTools. Unsure what to expect, I think I have been pretty thorough with writing my code. I tested in an incognito window so that my personal extensions on Chrome did not affect the test.
    + Lighthouse shows a performance score of:
        - 67 for Performance
            I looked into the reason for this score being lower than expected and found that it is mostly because I am using kits through other websites. I have elected to not worry about these as they allow my site to function smoothly at the moment.
        - 98 for Accessability
        - 100 for Best Practices
        - 91 for SEO
    + See below for a screenshot of my performance testing:
    + ![Lighthouse testing](static/images/lighthouse.png)
+ Checked all python code with CI Linter:
    + No major errors just line spacing and small formatting issues.
+ I have gone through all my models and views to ensure they have docstrings for readability.

## Security

+ All secret keys are handled through `.gitignore` initially, then with a `.env` file for local deployment, then finally through config vars in Heroku.
+ Data storage is done through Heroku and Cloudinary using secret keys as described above and PostgreSQL within config vars and `.env` file.
+ I've used Crispy forms to generate unique tokens for each user session. Then each form has to include this token for Django to validate it. If the token is missing due to malicious information, or its invalid/missing, then the message will be automatically rejected thanks to Crispy forms.
+ I've also used `allauth` for user authentication to ensure that casual visitors or people with malicious intent cannot make adjustments or comments on the website.
+ `ALLOWED_HOSTS` is the first layer of security for my site as it tells Django which domain names are allowed to serve this application. In this case I have only used Heroku and localhost to limit malicious activity as much as possible.

## Re submission follow ups:

+ As a result of some broken links I have been requested to do a resubmission, please see all following notes for what was done in this period.

### Competition page

+ It is always important to admit when you have gone a little too far. When initially I created the idea for this page i thought it would be nice to have a page where people could post their tanks and compete at different levels for prizes. Unfortunately I never really got it to work properly, but also it was an unneccesary addition to a page that already had multiple levels and different app types. As a result of this and with some advice from my tutor I made the decision to remove the entire app and all associated links. The only issue this really caused was a lack of symmetry on the home page. If I was to go back to the page and go at it again I would definitely look to integrate a competition page but possibly matching it with the social section to merge it better.

### Broken links

+ The first links noticed by the examiners were the one in this README file. When I looked into the formatting for the image paths in this file i found that when i had right clicked to 'copy relative path' it had automatically put back slashes into the file path rather than forward slashes meaning the .md file couldn't properly read the path. Once I had found the source of that initial issue, it was easy to go through and correct the remaining paths within the README file.
+ 

### Schema

+ I needed to add a visual for my Schema so I asked CoPilot to create an image based on my text based schema to show the flow of the keys on the site.

### CRUD

+ The 'Update' and 'Delete' aspects of my community posts were not working and were lacking on the posts themselves for logged in users. The first fix for this was to add the buttons for logged in users on their own posts. I also made sure to use Bootstrap styling to clean the look generally. See below for screenshots of those edits in action:
    + ![Testing buttons](static\images\testing-community.png)
+ Getting a screenshot of the edit and delete functions in action is more challenging than I thought it would be. I have added a screenshot of the messages that come up when in action though:
    + ![Testing functions](static\images\testing-crud.png)
+ Issue with loading images correctly through AWS cloud storage was due to me having not added the right policy in when setting it up originally. Once I added the policy into AWS S3 it was happy to load and show the images perfectly.
+ Navigation issues for the marketplace section. I had realised that when looking at the detail view for products there was only a button for customers to be able to buy the product, but not a button for them to return to the marketplace to carry on shopping. Added that button meaning better UI navigation for the clients. I also mirrored this idea at the basket point for customers to be able to 'Continue shopping' after adding something to their basket without having to go back to the navbar.
+ To bolster the navigation issues found in previous testing I have manually worked through the payment process and ensured I can go through the whole process from start to finish.

### Authentication

+ I had an issue with authenticated users being able to navigate to the log in page when already logged in. This was easily fixed using an accounts app and a full redirect to home page with a message to explain that this is what was happening. You can see screenshots of it in action below:
    + ![Authentication testing](static\images\authentication-testing.png)

### Navigation Smoke Test:

The following smoke test was carried out on the live deployed site to confirm that all primary navigation links and core user journeys function without server errors.

| Area Tested | Page / Route | Test Steps | Expected Behaviour | Actual Behaviour | Status |
|-------------|--------------|------------|--------------------|------------------|--------|
| Navigation | Home (`/`) | Click "Home" in navbar | Home page loads with no errors | Home page loaded with no errors | Pass |
| Navigation | Marketplace (`/marketplace/`) | Click "Marketplace" in navbar | Marketplace page loads and products display | Marketplace page loaded with no errors and products are displayed as expected | Pass |
| Navigation | Basket (`/basket/`) | Click "Basket" in navbar | Basket page loads; empty basket message if no items | Basket page loads correctly and in the test there was no items in basket and the page reflects this correctly | Pass |
| Navigation | Community (`/community/`) | Click "Community" in navbar | Community list loads with posts visible | It does load with all posts available however images are not loading. Looking into this further I found many issues, please see *Fixing AWS* for an explanation of the work done to resolve this | Pass (eventually) |
| Navigation | Gallery (`/gallery/`) | Click "Gallery" in navbar | Gallery page loads with no errors | Gallery loads with all images and styles correct | Pass |
| Authentication | Login (`/accounts/login/`) | Visit while logged out | Login page loads normally | Login page loads correctly with no issues | Pass |
| Authentication | Login (logged in) | Visit `/accounts/login/` while logged in | Redirects to home with message | Correctly redirects to Homepage with a message saying already logged in | Pass |
| Authentication | Signup (`/accounts/signup/`) | Visit while logged out | Signup page loads normally | Sign up page loads perfectly with no issues | Pass |
| Authentication | Signup (logged in) | Visit `/accounts/signup/` while logged in | Redirects to home with message | Correctly redirects to Homepage with a message saying already logged in | Pass |
| CRUD | Community Create | Create a new post | Post appears in list and detail view | New post created and confirmed to be formatting correctly | Pass |
| CRUD | Community Edit | Edit an existing post | Changes appear immediately in UI | All changes done through edit are working perfectly | Pass |
| CRUD | Community Delete | Delete a post | Post is removed from list | Post deleted as requested with a message informing as such | Pass |
| Basket | Add to Basket | Add item from Marketplace | Basket count updates; item appears in basket | Item appears in basket, and when quantity is updated it also updated in basket count in navbar | Pass |
| Checkout | Successful Payment | Complete checkout with Stripe test card | Redirect to success page; order recorded | Redirected to success page and order recorded on account | Pass |
| Validators | HTML/CSS Validation | Run W3C validators on key pages | No critical errors | base.html checked with one error and one warning, both of which ackowledged in README to be left. Full CSS file checked with no errors | Pass |
| Lighthouse | Performance & Accessibility | Run Lighthouse on home + key pages | Acceptable scores (e.g. >70) | ![Lighthouse testing results](static\images\LighthouseV2.png) | Pass |

## Fixing AWS

### **Summary of AWS S3 + Heroku Static & Media Configuration**

This project was updated to use Amazon S3 for hosting both static and media files in production. The following steps were completed to ensure Django, Heroku, and S3 work together correctly.

### **1. Enabled S3 for Static and Media Files**

Added an AWS configuration block in `settings.py` that activates when `USE_AWS=True` (set in Heroku Config Vars). This block:

- Defines the S3 bucket and region  
- Sets up Django 5’s `STORAGES` dictionary for static files  
- Configures `DEFAULT_FILE_STORAGE` for media files  
- Sets correct `STATIC_URL` and `MEDIA_URL` pointing to S3  
- Ensures caching and ACL settings are compatible with S3  
- Includes `STATICFILES_DIRS` so Django can find project‑level static files in production  

This ensures:

- **Static files** → uploaded to `static/` in S3  
- **Media files** → uploaded to `media/` in S3  
- Heroku no longer attempts to serve static/media locally  

### **2. Created Custom Storage Backends**

Added `custom_storages.py` with two classes:

- `StaticStorage` → handles static files  
- `MediaStorage` → handles media uploads  

Both classes disable ACLs and set correct S3 locations.

This allows Django to route static and media files to the correct S3 folders.

### **3. Fixed Static File Discovery in Production**

Heroku was not collecting static files because Django could not see the project’s `/static/` directory.

Solution:

```python
STATICFILES_DIRS = [BASE_DIR / "static"]
```

This was added to **both** the AWS and local development blocks.

Result:  
CSS, JS, and static images now upload correctly to S3 during Heroku builds.

### **4. Corrected Template Static Paths**

Some templates referenced static images using hard‑coded paths like:

/static/images/filename.png

These were updated to use Django’s static tag:

```django
{% static 'images/filename.png' %}
```

This ensures Django rewrites URLs to the S3 domain in production.

### **5. Fixed Media File Handling**

Gallery images and admin thumbnails were failing because:

- They were uploaded before S3 was enabled  
- They existed only in the old local `/media/` folder  
- Heroku cannot serve local media  

After enabling `DEFAULT_FILE_STORAGE` and `MEDIA_URL`, new uploads correctly save to S3.

Older images were re‑uploaded so they exist in the S3 `media/` folder.

### **6. Verified Heroku Build Behaviour**

During deployment:

- Heroku runs `collectstatic`  
- Static files are uploaded to S3  
- Media files are handled by the MediaStorage backend  
- The admin panel now loads correctly  
- Gallery images display as expected  

## **Outcome**

The project now uses a fully functional, production‑ready S3 setup:

- Static files load from `https://<bucket>.s3.amazonaws.com/static/...`  
- Media files load from `https://<bucket>.s3.amazonaws.com/media/...`  
- Heroku no longer serves static/media locally  
- Admin and gallery pages work correctly  
- All templates reference static assets properly  

This completes the migration from local file handling to cloud‑based storage.

## Stripe Webhook Endpoint Testing

### Webhook Configuration

The project uses a Stripe webhook to verify and process successful payments.  
The webhook endpoint is:

```
/checkout/wh/
```

This endpoint is defined in `checkout/urls.py` and handled by the `stripe_webhook` view.

The webhook signing secret is stored securely in environment variables:

- **Local:** `.env` → `STRIPE_WEBHOOK_SECRET`
- **Production:** Heroku Config Vars → `STRIPE_WEBHOOK_SECRET`

### 🧪 Webhook Test Procedure  
To verify that the webhook was correctly configured and functioning in production, the following steps were performed:

**1. Trigger a Test Payment (Stripe Test Mode)**
A test order was placed using Stripe’s test card:

- Card number: `4242 4242 4242 4242`  
- Any future expiry date  
- Any CVC  

This creates a real `payment_intent.succeeded` event in Stripe Test Mode.

**2. Stripe Automatically Sends the Webhook Event**
After the test payment completes, Stripe sends a POST request to:

```
https://<heroku-app>/checkout/wh/
```

**3. View Logs in Heroku Dashboard**
Since the Heroku CLI was not available on this machine, logs were viewed via:

*Heroku Dashboard → More → View Logs*

The logs showed Stripe successfully reaching the webhook endpoint and the Django view returning a `200 OK` response.

### Evidence of Working Webhook  
Below is the exact log output confirming the webhook was received and processed successfully:

```
POST /checkout/wh/ HTTP/1.1" 200
"Stripe/1.0 (+https://stripe.com/docs/webhooks)"
```

This demonstrates:

- The webhook URL is correct  
- Stripe reached the endpoint  
- The signature was verified  
- The event was processed without errors  
- Django returned a valid `200` response  

### Notes  
- A 404 was initially returned due to a mismatch between the environment variable name and the value referenced in `settings.py`.  
- After correcting the variable (`STRIPE_WEBHOOK_SECRET`) and redeploying, the webhook processed successfully.  
- The webhook view includes error handling for invalid payloads and missing signatures.

### Screenshots relevant to the above testing:

+ ![Stripe Endpoint sandbox](static\images\stripe-endpoint.png)
+ ![Stripe event locations](static\images\stripe-events.png)
+ ![Successful stripe events](static\images\stripe-success.png)
+ ![Successful Stripe log in Heroku](static\images\stripe-success-log.png)

## **Manual Test Matrix (With Verified Pass/Fail)**

### **Basket & Checkout Flow**

| Feature | Test Description | Expected Result | Pass/Fail |
|----------|------------------|-----------------|-----------|
| Add to Basket | User adds a product to the basket | Basket updates and item appears | Pass |
| Update Basket Quantity | User adjusts quantity | Totals update correctly | Pass |
| Remove Item | User removes an item | Item removed and totals update | Pass |
| Empty Basket Checkout | User tries to checkout with empty basket | User prevented from checking out | Pass |
| Checkout Page Loads | User proceeds to checkout | Checkout form loads with correct totals | Pass |
| Stripe Payment Success | User enters valid test card | Payment succeeds, redirected to success page | Pass |
| Stripe Payment Failure | User enters failing test card | Error message shown | Pass |
| Webhook Processing | Stripe sends `payment_intent.succeeded` | Webhook returns 200 and logs success | Pass |

*Screenshots for the above, not covered previously*
+ ![Stripe failure](static\images\stripe-failure.png)

### **User Accounts & Authentication**

| Feature | Test Description | Expected Result | Pass/Fail |
|----------|------------------|-----------------|-----------|
| Register Account | User signs up | Account created and logged in | Pass |
| Login | User logs in | Successful authentication | Pass |
| Logout | User logs out | Session ends, redirect occurs | Pass |
| Invalid Login | Wrong password | Error message shown | Pass |
| Authenticated Redirect | Logged‑in user visits login/signup | Redirected to dashboard | Pass |

### **Order Management**

| Feature | Test Description | Expected Result | Pass/Fail |
|----------|------------------|-----------------|-----------|
| Order Creation | Successful payment creates order | Order appears in admin | Pass |
| Order Detail Page | User views order detail | Correct order info displayed | Pass |
| Order Number in Success URL | Success page shows correct order number | Matches Stripe intent metadata | Pass |

### **Gallery & Community Features**

| Feature | Test Description | Expected Result | Pass/Fail |
|----------|------------------|-----------------|-----------|
| View Gallery | User visits gallery | Images load correctly | Pass |
| Community Create | Authenticated user creates post | Post appears in list | Pass |
| Community Edit | User edits their post | Changes saved | Pass |
| Community Delete | User deletes their post | Post removed | Pass |
| Permission Check | User tries to edit/delete others’ posts | Action blocked | Pass |

### **Navigation & UX**

| Feature | Test Description | Expected Result | Pass/Fail |
|----------|------------------|-----------------|-----------|
| Navbar Links | All navbar links tested | All links route correctly | Pass |
| Footer Links | Footer links tested | All links route correctly | Pass |
| Mobile Navigation | Navbar collapses on mobile | Menu opens/closes correctly | Pass |

### **Responsive Design**

| Device Size | Test Description | Expected Result | Pass/Fail |
|--------------|------------------|-----------------|-----------|
| Mobile | Test pages on mobile viewport | Layout adapts, no overflow | Pass |
| Tablet | Test pages on tablet viewport | Layout adapts correctly | Pass |
| Desktop | Test pages on desktop viewport | Full layout displays correctly | Pass |

### **Security & Validation**

| Feature | Test Description | Expected Result | Pass/Fail |
|----------|------------------|-----------------|-----------|
| Form Validation | Required fields blank | Error messages shown | Pass |
| CSRF Protection | Forms include CSRF tokens | Tokens present | Pass |
| URL Tampering | User tries restricted pages | Access denied or redirected | Pass |

### **Deployment & Webhooks**

| Feature | Test Description | Expected Result | Pass/Fail |
|----------|------------------|-----------------|-----------|
| Stripe Webhook Delivery | Stripe sends test event | Heroku logs show 200 OK | Pass |
| Environment Variables | Heroku config vars correct | App loads without errors | Pass |
| Static & Media Files | S3 bucket serving files | Images load correctly | Pass |
