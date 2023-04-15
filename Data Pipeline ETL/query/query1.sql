SELECT a.order_id,
	a.customer_id,
	a.order_status,
	order_purchase_timestamp,
	order_approved_at,
	order_delivered_carrier_date,
	order_delivered_customer_date,
	a.order_estimated_delivery_date,
	b.shipping_limit_date,
	b.order_item_id,
	b.product_id,
	b.price,
	b.freight_value,
	c.payment_type,
	c.payment_value,
	d.review_id,
	d.review_score

FROM tb_order a
    INNER JOIN tb_order_item b ON a.order_id = b.order_id
    INNER JOIN tb_order_payment c ON a.order_id = c.order_id
    INNER JOIN tb_order_review d ON a.order_id = d.order_id

LIMIT 2000;


