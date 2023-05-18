import requests
import csv
import gzip

data = requests.get(
    "https://productdata.awin.com/datafeed/download/apikey/ceeddca9eb1a8117d71200c0fcd73db5/language/any/fid/51903,57323,60419/columns/aw_deep_link,product_name,aw_product_id,merchant_product_id,merchant_image_url,description,merchant_category,search_price,merchant_name,merchant_id,category_name,category_id,aw_image_url,currency,store_price,delivery_cost,merchant_deep_link,language,last_updated,display_price,data_feed_id,brand_name,brand_id,colour,product_short_description,specifications,condition,product_model,model_number,dimensions,keywords,promotional_text,product_type,commission_group,merchant_product_category_path,merchant_product_second_category,merchant_product_third_category,in_stock,stock_quantity,valid_from,valid_to,is_for_sale,web_offer,pre_order,stock_status,size_stock_status,size_stock_amount,merchant_thumb_url,large_image,alternate_image,aw_thumb_url,alternate_image_two,alternate_image_three,alternate_image_four,reviews,average_rating,rating,number_available,custom_1,custom_2,custom_3,custom_4,custom_5,custom_6,custom_7,custom_8,custom_9,ean,isbn,upc,mpn,parent_product_id,product_GTIN,basket_link/format/csv/delimiter/%2C/compression/gzip/"
)
decompressed = gzip.decompress(data.content).decode()

reader = csv.DictReader(decompressed.splitlines(), delimiter=',')
cars = [*reader]