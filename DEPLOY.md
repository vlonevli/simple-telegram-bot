# Deploying to Render

You have two main options to deploy this bot.

## Option 1: Using Render CLI (If installed)

1.  Run the following command in your terminal:
    ```powershell
    render blueprint launch
    ```
2.  Follow the prompts to link your repository and deploy.

## Option 2: Using Git & Render Dashboard (Most Common)

1.  **Push your code to GitHub/GitLab/Bitbucket**:
    - Create a new repository on GitHub.
    - Setup the remote and push:
      ```powershell
      git remote add origin <your-github-repo-url>
      git push -u origin master
      ```

2.  **Create Service on Render**:
    - Go to [dashboard.render.com](https://dashboard.render.com).
    - Click **New +** -> **Blueprints**.
    - Connect your repository.
    - Render will automatically detect `render.yaml` and set everything up.

3.  **Set your Token**:
    - During setup, Render might ask for `TELEGRAM_TOKEN`. Paste your bot token there.
    - If not asked, go to the Service settings -> **Environment** and add `TELEGRAM_TOKEN`.

## Important Notes

- **The Web Server**: Your bot runs a small web server on port 5000 (or whatever Render assigns). This is required because Render's free tier (and paid Web Services) expects a web server to bind to a port within 60 seconds, or it considers the deploy failed. Use `https://<your-app-name>.onrender.com` to check if it says "Bot is alive!".
- **Logs**: Check the "Logs" tab in Render to see "Starting Bot..." and any errors.
