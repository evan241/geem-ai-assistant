FROM scratch

ARG MINIO_RELEASE=RELEASE.2025-09-07T16-13-09Z

ADD --chmod=0755 \
    https://dl.min.io/server/minio/release/linux-amd64/archive/minio.${MINIO_RELEASE} \
    /usr/bin/minio

EXPOSE 9000 9001

ENTRYPOINT ["/usr/bin/minio"]
CMD ["server", "/data", "--console-address", ":9001"]
