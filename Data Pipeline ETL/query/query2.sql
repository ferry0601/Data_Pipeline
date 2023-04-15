SELECT e.product_id,
        e.product_category_name,
        f.product_category_name_english

FROM tb_product e
    INNER JOIN tb_product_category_name f ON e.product_category_name = f.product_category_name

LIMIT 2000;