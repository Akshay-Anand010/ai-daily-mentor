# Deployment

## Recommended: Render or Railway

1. Create a new private GitHub repository and push this project.
2. In Render, create a Blueprint from the repository (the `render.yaml` file is included), or create a Railway service using `railway.toml`.
3. Add a managed PostgreSQL database and configure `DATABASE_URL`, `SECRET_KEY`, `OPENAI_API_KEY`, `FRONTEND_ORIGIN`, and email provider credentials.
4. Deploy the API, then deploy the Next.js frontend with `NEXT_PUBLIC_API_URL=https://your-api.example.com` set at build time.
5. Set `FRONTEND_ORIGIN` to the deployed frontend URL and redeploy the API.

## Email delivery

Use Resend or SMTP with a verified sending domain. Never put provider keys in the frontend. Add them only as host environment variables. The present subscription endpoint stores opt-ins; before sending campaigns, add a verified double-opt-in flow, unsubscribe endpoint, privacy policy, and compliance review appropriate to your audience and jurisdiction.

## GitHub Pages

Pages can host a static marketing site but cannot run the API, scheduler, database, or secure subscription endpoint. Point any Pages-hosted frontend at the Render/Railway backend via `NEXT_PUBLIC_API_URL`; deploy the frontend separately if you need server rendering.
