# API Dashboard

This project automatically fetches data from an API and displays it on a static website. The data is updated periodically using GitHub Actions.

## How It Works

1. A GitHub Actions workflow runs on a schedule (every 6 hours by default)
2. It executes the `update_data.py` script which:
   - Queries the API
   - Generates a fresh HTML file with the latest data
3. The updated HTML file is committed and pushed to the repository
4. GitHub Pages or Netlify serves the static file

## Setup Instructions

### For GitHub Pages:

1. Create a new repository and upload these files
2. Go to repository Settings → Pages
3. Select "GitHub Actions" as the source
4. Your site will be available at `https://yourusername.github.io/repository-name/`

### For Netlify:

1. Sign up/login to Netlify
2. Click "New site from Git"
3. Select your GitHub repository
4. Set build command to `echo "No build needed"`
5. Set publish directory to the repository root

## Customization

- Modify `update_data.py` to connect to your specific API
- Adjust the update frequency by changing the cron expression in `.github/workflows/update-data.yml`
- Customize the HTML template in the `generate_html` function
