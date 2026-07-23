FROM node:20-alpine

RUN corepack enable \
    && corepack prepare pnpm@9.15.4 --activate

WORKDIR /app

COPY apps/web/package.json ./

RUN pnpm install --no-frozen-lockfile

COPY apps/web ./

CMD ["pnpm", "dev", "--host", "0.0.0.0"]