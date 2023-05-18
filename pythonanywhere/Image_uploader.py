import cloudinary
import cloudinary.uploader
cloudinary.config( 
  cloud_name = "db0kzjtgs", 
  api_key = "327478757255189", 
  api_secret = "nYe7sbLMsViWWntcMuQuOkCoStI",
  secure = True
)

CLOUDINARY_URL = "cloudinary://327478757255189:nYe7sbLMsViWWntcMuQuOkCoStI@db0kzjtgs"
url="https://akamai.vgc.no/drfront/images/2021/10/01/w=1080;h=710;636204.jpg"
test=cloudinary.uploader.upload("https://akamai.vgc.no/drfront/images/2021/10/01/w=1080;h=710;636204.jpg", folder="vg", overwrite=False, public_id="".join(url.split("/")[-1]))