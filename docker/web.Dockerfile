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


FROM nginxinc/nginx-unprivileged:1.30.5-alpine3.24@sha256:ed04ec1ff34502c339ee5c3ae3f855442398edc1d05591e2b98981dcbbd20b1e AS production

COPY --from=builder /app/dist /usr/share/nginx/html

EXPOSE 8080
