create table tb_customer (
	customer_id text,
	customer_unique_id text,
	customer_zip_code_prefix int not null,
	customer_city text,
	customer_state text

);

create table tb_geolocation (
	geolocation_zip_code_prefix int not null,
	geolocation_lat float,
	geolocation_lng float,
	geolocation_city text,
	geolocation_state text

);

create table tb_order_item (
	order_id text,
	order_item_id int not null,
	product_id text,
	seller_id text,
	shipping_limit_date timestamp,
	price float,
	freight_value float

);

create table tb_order_payment (
	order_id text,
	payment_sequential int not null,
	payment_type text,
	payment_installments int not null,
	payment_value float

);

create table tb_order_review ( 
	review_id text,
	order_id text,
	review_score int not null,
	review_comment_title text,
	review_comment_message text,
	review_creation_date timestamp,
	review_answer_timestamp timestamp

);

create table tb_order(
	order_id text,
	customer_id text,
	order_status text,
	order_purchase_timestamp timestamp,
	order_approved_at timestamp,
	order_delivered_carrier_date timestamp,
	order_delivered_customer_date timestamp,
	order_estimated_delivery_date timestamp

);

create table tb_product_category_name (
	product_category_name text,
	product_category_name_english text
);

create table tb_product (
	product_id text,
	product_category_name text,
	product_name_lenght float,
	product_description_lenght float,
	product_photos_qty float,
	product_weight_g float,
	product_length_cm float,
	product_height_cm float,
	product_width_cm float

);

create table tb_seller (
	seller_id text,
	seller_zip_code_prefix int not null,
	seller_city text,
	seller_state text

);