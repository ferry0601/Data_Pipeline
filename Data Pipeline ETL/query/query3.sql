SELECT g.customer_id,
    g.customer_city,
    h.seller_id,
    h.seller_city,
    i.geolocation_zip_code_prefix

FROM tb_customer g
    INNER JOIN tb_seller h ON g.customer_zip_code_prefix = h.seller_zip_code_prefix
    INNER JOIN tb_geolocation i ON g.customer_zip_code_prefix = i.geolocation_zip_code_prefix

LIMIT 2000;
    