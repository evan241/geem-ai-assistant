FROM node:20-alpine@sha256:fb4cd12c85ee03686f6af5362a0b0d56d50c58a04632e6c0fb8363f609372293 AS base

ENV COREPACK_HOME=/opt/corepack

RUN mkdir -p "${COREPACK_HOME}" \
    && chown -R node:node "${COREPACK_HOME}" \
    && corepack enable \
    && corepack prepare pnpm@9.15.4 --activate

WORKDIR /app

COPY --chown=node:node apps/web/package.json apps/web/pnpm-lock.yaml ./

RUN pnpm install --frozen-lockfile

COPY --chown=node:node apps/web ./


FROM base AS development

RUN mkdir -p /app/node_modules \
    && chown -R node:node /app

USER node

CMD ["pnpm", "dev", "--host", "0.0.0.0"]


FROM base AS builder

RUN pnpm build


FROM nginxinc/nginx-unprivileged:alpine@sha256:18d67281256ded39ff65e010ae4f831be18f19356f83c60bc546492c7eb6dd23 AS production

COPY --from=builder /app/dist /usr/share/nginx/html

EXPOSE 8080
