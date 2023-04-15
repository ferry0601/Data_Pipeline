from mrjob.job import MRJob
from mrjob.step import MRStep

import csv
import json

cols = 'order_id,customer_id,order_status,order_purchase_timestamp,order_estimated_delivery_date,shipping_limit_date,order_item_id,product_id,price,freight_value,payment_type,payment_value,review_id,review_score'.split(',')
 
def csv_readline(line):
    for row in csv.reader([line]) :
        return row
class OrderDateCount(MRJob):
    def steps(self):
        return[
            MRStep(mapper=self.mapper, reducer=self.reducer),
            MRStep(reducer=self.sort)
        ]

    def mapper(self, _, line):
        row = dict(zip(cols, csv_readline(line)))

        if row['order_id'] != 'order_id':
            yield row['order_estimated_delivery_date'][0:200], 1

    def reducer(self, key, values):
        yield None, (key, sum(values))

    def sort(self, key, values):
        data=[]
        for order_estimated_delivery_date, order_count in values:
            data.append((order_estimated_delivery_date, order_count))
            data.sort()

        for order_estimated_delivery_date, order_count in data:
            yield order_estimated_delivery_date, order_count



if __name__ == '__main__':
    OrderDateCount.run()