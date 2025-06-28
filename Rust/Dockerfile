FROM rust:1.88 AS builder

# نصب musl-tools برای کامپایل استاتیک
RUN apt-get update && apt-get install -y musl-tools

WORKDIR /app
COPY Cargo.toml Cargo.lock ./
COPY src ./src

RUN rustup target add x86_64-unknown-linux-musl
RUN cargo build --release --target x86_64-unknown-linux-musl

FROM scratch
COPY --from=builder /app/target/x86_64-unknown-linux-musl/release/actix_hello /actix_hello
ENTRYPOINT ["/actix_hello"]
