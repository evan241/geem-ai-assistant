FROM golang:1.24.6-bookworm AS builder

ARG MINIO_RELEASE=RELEASE.2025-09-07T16-13-09Z

RUN git clone \
        --branch "${MINIO_RELEASE}" \
        --depth 1 \
        https://github.com/minio/minio.git \
        /src/minio \
    && test "$(git -C /src/minio describe --tags --exact-match)" = "${MINIO_RELEASE}"

WORKDIR /src/minio

RUN mkdir -p /out \
    && CGO_ENABLED=0 go build -trimpath -o /out/minio .

FROM scratch

COPY --from=builder /out/minio /usr/bin/minio

EXPOSE 9000 9001

ENTRYPOINT ["/usr/bin/minio"]
CMD ["server", "/data", "--console-address", ":9001"]
