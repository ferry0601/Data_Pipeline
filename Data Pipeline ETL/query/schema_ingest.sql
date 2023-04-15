DROP TABLE IF EXISTS dim_market;
CREATE TABLE dim_market(
    order_id text,
    customer_id text,
	order_status text,
	order_purchase_timestamp timestamp,
	order_estimated_delivery_date timestamp,
	shipping_limit_date timestamp,
	order_item_id int not null,
	product_id text,
	price float,
	freight_value float,
	payment_type text,
	payment_value float,
    review_id text,
	review_score int not null
);


