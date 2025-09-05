from simple_image_download import simple_image_download as simp

response = simp.simple_image_download

# Download 10 images of water logging
response().download("pipe burst", 10)