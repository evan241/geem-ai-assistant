FROM node:20-alpine

RUN corepack enable

WORKDIR /app

COPY apps/web/package.json apps/web/pnpm-lock.yaml* ./
RUN pnpm install

COPY apps/web ./

CMD ["pnpm", "dev", "--host", "0.0.0.0"]
