from wing import *

def bucket_oncreate_handler(event, context):
  print("a more friendly print")
  print(event)
  print(context)
  initial_image = lifted("media-app-initial-image")
  resized_image = lifted("media-app-resized-image")
  resized_image.put("2.png", initial_image.get("1.png"))


  