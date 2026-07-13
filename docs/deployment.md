# Deployment

## Recommended: Render or Railway

1. Create a new GitHub repository and push this project.
2. In Render, create a Blueprint from the repository (the `render.yaml` file is included), or create a Railway service using `railway.toml`.
3. Add a managed PostgreSQL database and configure `DATABASE_URL`, `SECRET_KEY`, `OPENAI_API_KEY`, `FRONTEND_ORIGIN`, and email provider credentials.
4. Deploy the API, then deploy the Next.js frontend with `NEXT_PUBLIC_API_URL=https://your-api.example.com` set at build time.
5. Set `FRONTEND_ORIGIN` to the deployed frontend URL and redeploy the API.

## Email delivery

Use Resend or SMTP with a verified sending domain. Never put provider keys in the frontend. Add them only as host environment variables. The present subscription endpoint stores opt-ins; before sending campaigns, add a verified double-opt-in flow, unsubscribe endpoint, privacy policy, and compliance review appropriate to your audience and jurisdiction.

## GitHub Pages public site

The included `deploy-pages.yml` workflow publishes the frontend whenever `main` changes. In GitHub, open **Settings → Pages → Build and deployment**, select **GitHub Actions**, then open **Settings → Secrets and variables → Actions → Variables** and create:

```text
NEXT_PUBLIC_API_URL=https://your-api.onrender.com
```

Set the backend's `FRONTEND_ORIGIN` to `https://akshay-anand010.github.io` (the origin only—do not include `/ai-daily-mentor`). Commit and push the workflow changes. The public site will be at `https://akshay-anand010.github.io/ai-daily-mentor/`.

Pages only serves the static website. The API, PostgreSQL database, scheduler, and secure subscription endpoint remain on Render or Railway; this separation is required for real subscriptions and daily emails.
