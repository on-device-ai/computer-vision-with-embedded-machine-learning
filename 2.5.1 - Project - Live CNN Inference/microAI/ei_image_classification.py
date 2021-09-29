import tflite
import microai
import array
import sys

tflite.initialize_target();
tflite.setup_error_reporter();
if microai.load_model_from_file('/userdata/trained.tflite') is False :
  sys.exit()
tflite.build_interpreter()
if tflite.allocate_tensors() is False :
  sys.exit()
  
img_w    = 48
img_h    = 48
img_ch   = 1
img_size = img_w * img_h * img_ch

input_tensor  = array.array('b',[0] * img_size)
output_tensor = array.array('b',[0,0])

while True :
  microai.get_image(img_w,img_h,img_ch,input_tensor)
  microai.set_input_tensor_value(input_tensor)
  if tflite.interpreter_invoke() is False :
    sys.exit()
  microai.get_output_tensor_value(output_tensor) 
  background_score = output_tensor[0]
  dog_score = output_tensor[1]
  print("background_score = %d , dog_score = %d" % (background_score,dog_score))