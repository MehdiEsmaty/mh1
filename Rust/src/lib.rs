use actix_web::{get, HttpResponse, Responder};

#[get("/")]
pub async fn hello() -> impl Responder {
    HttpResponse::Ok().body("Hello from Rust!")
}

#[cfg(test)]
mod tests {
    use super::*;
    use actix_web::{body::to_bytes, http::StatusCode, test, App};

    #[actix_web::test]
    async fn test_hello_route() {
        let app = test::init_service(App::new().service(hello)).await;
        let req = test::TestRequest::get().uri("/").to_request();
        let resp = test::call_service(&app, req).await;

        assert_eq!(resp.status(), StatusCode::OK);

        let body = to_bytes(resp.into_body()).await.unwrap();
        assert_eq!(body, "Hello from Rust!");
    }
}
